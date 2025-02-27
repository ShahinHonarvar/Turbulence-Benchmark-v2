def prime_factors(lst):

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors_lst(num):
        factors = []
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                factors.append(i)
        return factors
    return set(prime_factors_lst(lst[78]))