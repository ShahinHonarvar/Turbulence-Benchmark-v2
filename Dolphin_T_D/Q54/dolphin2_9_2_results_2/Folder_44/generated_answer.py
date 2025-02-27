def all_right_truncatable_prime(x):

    def is_right_truncatable_prime(n):
        while n != 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_prime(n):
        if n != 1:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
        return True
    primes = [n for n in range(2, x) if is_prime(n)]
    return sorted([p for p in primes if is_right_truncatable_prime(p)])