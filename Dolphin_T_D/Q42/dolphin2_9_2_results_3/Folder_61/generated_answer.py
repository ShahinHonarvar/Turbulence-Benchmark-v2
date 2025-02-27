def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of_one_number(n):
        factors = set()
        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                factors.add(i)
        return factors
    if len(numbers) >= 9:
        return prime_factors_of_one_number(numbers[8])
    else:
        return set()