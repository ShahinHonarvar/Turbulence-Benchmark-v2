def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = n // 10
            if n % 10 == 0 or not is_prime(n):
                return False
        return True
    x = numbers[77]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes)