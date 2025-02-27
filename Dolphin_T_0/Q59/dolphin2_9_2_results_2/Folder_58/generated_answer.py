def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[975]
    primes = []
    if is_prime(x):
        primes.append(x)
    i = x - 1
    while i > 1:
        if is_prime(i):
            s = str(i)
            d = len(s) - 1
            while d > 0 and s not in primes:
                if int(s) not in primes and is_prime(int(s)):
                    primes.append(int(s))
                s = s[1:]
                d -= 1
        i -= 1
    return sorted(primes, reverse=True)