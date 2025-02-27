def prime_factors(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = []
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factors.append(i)
        return factors
    return set(get_factors(num_list[222]))