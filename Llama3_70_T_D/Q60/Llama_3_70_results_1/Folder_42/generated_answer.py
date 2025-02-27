def all_left_right_truncatable_prime(t):
    x = t[64]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = [i for i in primes if is_left_right_truncatable(i)]
    return sorted(truncatable_primes, reverse=True)