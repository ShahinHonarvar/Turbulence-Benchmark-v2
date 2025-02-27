def all_right_truncatable_prime(t):
    x = t[98]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            n = str(i)
            while len(n) > 1:
                n = n[:-1]
                if not is_prime(int(n)):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes)