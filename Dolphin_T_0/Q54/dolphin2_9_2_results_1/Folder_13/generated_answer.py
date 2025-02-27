def all_right_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n != 0:
            if not is_prime(n):
                return False
            if n % 10 == 0:
                n //= 10
            else:
                n = n // 10
        return True
    x = t[784]
    primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable(i):
            primes.append(i)
    return sorted(primes)