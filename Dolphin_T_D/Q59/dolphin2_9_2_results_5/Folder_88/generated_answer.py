def all_left_truncatable_prime(p):
    x = p[93]

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        if n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def is_truncatable(n):
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    primes = []
    for n in range(2, x):
        if is_truncatable(n):
            primes.append(n)
    return sorted(primes)