def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    x = t[20]
    primes = []
    for n in range(x, 0, -1):
        n_str = str(n)
        if '0' not in n_str:
            trunc = n_str
            while trunc:
                if not is_prime(int(trunc)):
                    break
                trunc = trunc[1:]
            else:
                primes.append(n)
    return sorted(primes, reverse=True)