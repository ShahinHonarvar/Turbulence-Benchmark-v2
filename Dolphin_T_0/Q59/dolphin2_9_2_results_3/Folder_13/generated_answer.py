def all_left_truncatable_prime(tup):
    x = tup[784]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(p):
        if '0' in str(p) or not is_prime(p):
            return False
        was_prime = is_prime(p)
        p = int(str(p)[1:])
        while p > 0:
            if not is_prime(p):
                return False
            p = int(str(p)[1:])
        return was_prime
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatables = [i for i in primes if is_truncatable(i)]
    return sorted(truncatables)