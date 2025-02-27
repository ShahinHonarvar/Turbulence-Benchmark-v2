def all_right_truncatable_prime(params):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 9:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = params[175]
    primes = [i for i in range(2, x) if is_prime(i) and is_truncatable(i)]
    return sorted(primes)