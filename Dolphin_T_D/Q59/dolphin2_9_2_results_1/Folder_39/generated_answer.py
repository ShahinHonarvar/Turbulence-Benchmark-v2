def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True
    x = t[30]
    primes = [i for i in reversed(range(2, x)) if is_prime(i)]
    left_truncatable_primes = []
    for p in primes:
        if all([is_prime(int(str(p)[i:])) for i in range(1, len(str(p)))]):
            left_truncatable_primes.append(p)
    return left_truncatable_primes