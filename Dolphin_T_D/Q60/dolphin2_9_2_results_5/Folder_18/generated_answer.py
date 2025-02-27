def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate(n):
        while n > 9:
            if not is_prime(n):
                return False
            if n % 10 == 0:
                return False
            n = int(n / 10)
        return is_prime(n)
    x = t[429]
    primes = [n for n in range(x, 0, -1) if truncate(n)]
    return primes