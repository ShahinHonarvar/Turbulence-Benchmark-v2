def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 9:
            n = n // 10
            m = n - n // 100 * 100
            if not is_prime(n) or not is_prime(m):
                return False
        return True
    trunc_primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and is_truncatable(i):
            trunc_primes.append(i)
    return trunc_primes