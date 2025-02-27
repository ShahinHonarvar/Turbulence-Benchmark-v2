def prime_factors(integers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    target = integers[23]
    factors = []
    for i in range(2, target + 1):
        if is_prime(i) and target % i == 0:
            factors.append(i)
    return set(factors)