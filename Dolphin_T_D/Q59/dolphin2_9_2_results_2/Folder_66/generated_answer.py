def all_left_truncatable_prime(t):
    primes = []
    x = t[25]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(p):
        p = str(p)
        for i in range(len(p) - 1, 0, -1):
            if is_prime(int(p[i:])) and (not '0' in p[:i]):
                continue
            return False
        return True
    for n in range(x - 1, 1, -1):
        if is_prime(n) and is_truncatable(n):
            primes.append(n)
    return sorted(primes, reverse=True)