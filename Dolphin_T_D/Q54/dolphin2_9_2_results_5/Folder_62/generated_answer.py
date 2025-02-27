def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[70]
    primes = [n for n in range(x) if is_right_truncatable_prime(n)]
    return sorted(primes)