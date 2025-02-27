def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def trunc(n):
        if n < 10:
            return True
        return is_prime(int(n / 10))
    x = t[29]
    primes = [i for i in range(2, x) if is_prime(i) and trunc(i)]
    return sorted(primes)