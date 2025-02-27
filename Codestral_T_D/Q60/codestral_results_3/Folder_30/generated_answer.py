def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        length = len(str(n))
        if length == 1:
            return is_prime(n)
        return is_prime(n) and is_left_right_truncatable_prime(int(str(n)[1:])) and is_left_right_truncatable_prime(int(str(n)[:-1]))
    x = numbers[37]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)