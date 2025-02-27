def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[69]
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i) and '0' not in str(i):
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)