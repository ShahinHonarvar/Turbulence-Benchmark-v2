def all_left_truncatable_prime(t):
    x = t[30]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(p):
        for i in range(len(str(p))):
            if not is_prime(int(str(p)[i:])):
                return False
        return True
    for i in range(10, x):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)