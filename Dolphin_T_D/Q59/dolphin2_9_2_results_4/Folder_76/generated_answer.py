def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(p):
        while p != 0 and is_prime(p):
            p //= 10
        return p == 0
    primes = [n for n in range(2, x) if is_prime(n) and is_truncatable(n) and (not '0' in str(n))]
    return primes[::-1]