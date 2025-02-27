def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[57]
    left_truncatable_primes = []
    for i in range(x - 1, 0, -1):
        if is_prime(i) and is_truncatable(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes