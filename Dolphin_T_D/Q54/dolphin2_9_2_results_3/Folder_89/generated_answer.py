def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[97]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatables = []
    for p in primes:
        if '0' not in str(p):
            if all((is_prime(int(str(p)[:j])) for j in range(1, len(str(p)) + 1))):
                truncatables.append(p)
    return sorted(truncatables, reverse=True)