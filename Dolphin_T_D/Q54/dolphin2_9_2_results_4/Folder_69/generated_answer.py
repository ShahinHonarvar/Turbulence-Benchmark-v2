def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
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

    def next_truncatable(n):
        while True:
            n -= 1
            if is_right_truncatable_prime(n):
                return n
    x = t[760]
    primes = []
    while x > 1:
        if is_right_truncatable_prime(x):
            primes.append(x)
        x = next_truncatable(x)
    return sorted(primes, reverse=True)