def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        str_n = str(n)
        if '0' in str_n:
            return False
        return is_prime(n) and is_left_right_truncatable_prime(int(str_n[1:])) and is_left_right_truncatable_prime(int(str_n[:-1]))
    x = numbers[23]
    left_right_truncatable_primes = []
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return sorted(left_right_truncatable_primes)