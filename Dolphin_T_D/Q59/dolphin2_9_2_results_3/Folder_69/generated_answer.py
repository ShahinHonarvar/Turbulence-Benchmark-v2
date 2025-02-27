def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(p):
        if p < 2 or p % 5 == 0 or p % 2 == 0:
            return False
        s = str(p)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = t[760]
    primes = [p for p in range(2, x) if is_prime(p) and is_left_truncatable(p)]
    return sorted(primes, reverse=True)