def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        a = 3
        while a * a <= n and n % a != 0:
            a += 2
            if a > n.bit_length():
                break
        return a * a != n

    def remove_digits(n):
        while n > 9 and is_prime(n):
            left_digit = n // 10 ** (n.bit_length() - 2)
            right_digit = n % 10
            n = n % 10 ** (n.bit_length() - 2) * 10 + n // 10 % 10
            if not is_prime(n):
                return False
            if not (left_digit == 2 or left_digit == 3 or left_digit == 5 or (left_digit == 7)):
                return False
            if not (right_digit == 2 or right_digit == 3 or right_digit == 5 or (right_digit == 7)):
                return False
        return True
    x = tup[38]
    primes = []
    for i in range(5, x + 1):
        if is_prime(i) and remove_digits(i):
            primes.append(i)
    return sorted(primes, reverse=True)