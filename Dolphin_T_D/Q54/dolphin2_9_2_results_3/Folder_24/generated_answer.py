def all_right_truncatable_prime(args):

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    x = args[65]
    primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(primes, reverse=True) if primes else []