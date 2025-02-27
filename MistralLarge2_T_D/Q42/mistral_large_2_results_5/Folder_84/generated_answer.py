def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors_set = set()
        for i in range(1, n + 1):
            if n % i == 0 and is_prime(i):
                factors_set.add(i)
        return factors_set
    if len(lst) <= 685:
        return set()
    return factors(lst[685])