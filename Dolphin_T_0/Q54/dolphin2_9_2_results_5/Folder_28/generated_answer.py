def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 2:
            return False
        x = n
        while x:
            x //= 10
            if not is_prime(x):
                return False
        return True
    x = t[19]
    primes = [i for i in range(x) if is_right_truncatable(i) and is_prime(i)]
    return sorted(primes)