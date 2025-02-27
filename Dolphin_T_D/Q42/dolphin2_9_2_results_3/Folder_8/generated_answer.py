def prime_factors(lst):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = []
        i = 2
        while i <= n:
            if n % i == 0 and is_prime(i):
                factors.append(i)
            i += 1
        return factors
    return set(get_factors(lst[49]))