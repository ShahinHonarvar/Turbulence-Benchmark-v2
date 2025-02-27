def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        m = int(n ** 0.5) + 1
        for x in range(3, m, 2):
            if n % x == 0:
                return False
        return True

    def right_truncatable(n):
        if is_prime(n):
            for d in range(1, len(str(n))):
                if not is_prime(n // 10 ** d):
                    return False
            return True
        else:
            return False
    primes = []
    for n in range(0, t[3]):
        if right_truncatable(n):
            primes.append(n)
    return sorted(primes, reverse=True)