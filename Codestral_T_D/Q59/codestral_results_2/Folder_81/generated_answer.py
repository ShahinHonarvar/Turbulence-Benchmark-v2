def all_left_truncatable_prime(t):
    x = t[98]
    primes = [2]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_left_truncatable_prime(truncate_left(n))
    for i in range(3, x, 2):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return primes