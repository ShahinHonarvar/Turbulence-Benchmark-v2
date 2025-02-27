def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n == 0:
            return False
        temp = n
        while temp:
            if not is_prime(temp):
                return False
            temp //= 10
        return True
    primes = [n for n in range(x) if is_left_truncatable(n)]
    return sorted(primes, key=int)