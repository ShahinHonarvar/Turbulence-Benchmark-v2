def all_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 9:
            if not is_prime(n // 10):
                return False
            n //= 10
        return True
    right_truncatable_primes = [n for n in range(x, 1, -1) if is_truncatable_prime(n)]
    return right_truncatable_primes