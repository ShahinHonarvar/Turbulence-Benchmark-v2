def all_left_truncatable_prime(t):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[6]
    primes = []
    for i in range(x, 0, -1):
        s = str(i)
        if '0' in s:
            continue
        f = True
        for j in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[j:])):
                f = False
                break
        if f:
            primes.append(i)
    return sorted(primes, reverse=True)