def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = tup[0]
    primes = [i for i in range(x - 1, 0, -1) if is_left_truncatable(i)]
    return primes