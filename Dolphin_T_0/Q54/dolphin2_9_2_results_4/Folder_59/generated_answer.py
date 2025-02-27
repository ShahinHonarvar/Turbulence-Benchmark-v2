def all_right_truncatable_prime(tup):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = tup[84]
    primes = {}
    for i in range(2, x + 1):
        if is_prime(i):
            primes[i] = is_truncatable_prime(i)
    return sorted([k for k, v in primes.items() if v], reverse=True)