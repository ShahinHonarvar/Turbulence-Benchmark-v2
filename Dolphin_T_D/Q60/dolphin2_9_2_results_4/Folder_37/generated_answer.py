def all_left_right_truncatable_prime(tup):
    x = tup[35]

    def is_truncatable_prime(n):
        if n < 2:
            return False
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                return False
        s = str(n)
        for _ in range(len(s) - 2):
            if s.startswith('0') or s.endswith('0'):
                return False
            s = s[1:-1]
            if not is_truncatable_prime(int(s)):
                return False
        return True
    primes = [i for i in range(x, 0, -1) if is_truncatable_prime(i)]
    primes.sort(reverse=True)
    return primes if primes else []