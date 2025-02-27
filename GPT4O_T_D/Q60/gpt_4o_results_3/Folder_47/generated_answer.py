def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    if len(t) <= 49:
        return []
    x = t[49]
    truncatable_primes = [p for p in range(10, x + 1) if is_prime(p) and '0' not in str(p) and is_truncatable_prime(p)]
    return sorted(truncatable_primes)