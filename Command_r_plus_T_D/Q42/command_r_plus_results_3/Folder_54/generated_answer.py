def prime_factors(numbers_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = []
        for i in range(2, n + 1):
            while n % i == 0:
                factors.append(i)
                n //= i
        return factors
    if len(numbers_list) > 51:
        target_number = numbers_list[51]
        prime_factors_list = get_prime_factors(target_number)
        prime_set = set((factor for factor in prime_factors_list if is_prime(factor)))
        return prime_set
    else:
        return set()