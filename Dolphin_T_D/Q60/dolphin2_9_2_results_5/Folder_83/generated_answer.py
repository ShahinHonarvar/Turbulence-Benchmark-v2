def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_truncatable(n):
        if n == 1:
            return False
        while n > 1:
            if is_prime(n):
                n = int(str(n)[1:-1])
            else:
                return False
        return True
    x = t[24]
    primes = []
    for n in range(x + 1):
        if is_truncatable(n) and is_prime(n):
            primes.append(n)
    primes.sort()
    return primes