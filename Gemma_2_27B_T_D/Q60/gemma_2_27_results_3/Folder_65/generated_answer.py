def all_left_right_truncatable_prime(t):
    x = t[32]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        s = str(i)
        truncatable = True
        while len(s) > 1:
            if not is_prime(int(s)):
                truncatable = False
                break
            s = s[1:-1]
        if truncatable and is_prime(i):
            primes.append(i)
    return sorted(primes)