def prime_factors(lst):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    target = lst[72]
    factors = set()
    for i in range(1, target + 1):
        if target % i == 0 and is_prime(i):
            factors.add(i)
    return factors