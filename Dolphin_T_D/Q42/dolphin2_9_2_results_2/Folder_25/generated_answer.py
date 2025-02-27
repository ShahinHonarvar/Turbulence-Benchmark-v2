def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target = lst[90]
    factors = set()
    for i in range(1, target + 1):
        if target % i == 0 and is_prime(i):
            factors.add(i)
    return factors