def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(p):
        while p > 0:
            if not is_prime(p):
                return False
            p = p // 10
        return True
    x = numbers[69]
    right_truncatable_primes = [p for p in range(2, x) if is_right_truncatable_prime(p)]
    return sorted(right_truncatable_primes, reverse=True)