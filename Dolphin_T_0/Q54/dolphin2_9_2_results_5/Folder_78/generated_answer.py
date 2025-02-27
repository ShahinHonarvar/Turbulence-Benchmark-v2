def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_right_truncatable(n):
        if len(n) == 1:
            return is_prime(int(n))
        if not is_prime(int(n)):
            return False
        return all_right_truncatable(n[:-1])
    x = t[23]
    primes = [str(i) for i in range(1, x) if is_prime(i)]
    right_truncatable = [p for p in primes if all_right_truncatable(p)]
    return sorted(right_truncatable)