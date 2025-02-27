def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n:
            if n % 10 % 2 == 0 or n[::-1][1:] % 10 % 2 == 0:
                n //= 10
                continue
            if not is_prime(n):
                return False
            n //= 10
        return True
    primes = [i for i in range(x) if is_prime(i)]
    return sorted([i for i in primes if is_right_truncatable_prime(i)])