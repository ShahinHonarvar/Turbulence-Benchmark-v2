def all_right_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n < 2:
            return False
        r = int(n ** 0.5)
        f = 3
        while f <= r:
            if n % f == 0:
                return False
            f += 2
        return True
    x = t[29]
    primes = [i for i in range(2, x) if is_prime(i)]
    r = [p for p in primes if all((is_prime(int(str(p)[-i - 1::-1])) for i in range(len(str(p)) - 1)))]
    return sorted(r)