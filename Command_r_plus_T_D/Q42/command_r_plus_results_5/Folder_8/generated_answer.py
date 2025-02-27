def prime_factors(numbers_list):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_prime_factors(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    if len(numbers_list) > 49:
        target_number = numbers_list[49]
        prime_factors_set = set(get_prime_factors(target_number))
        prime_factors_set = {factor for factor in prime_factors_set if is_prime(factor)}
        return prime_factors_set
    else:
        return set()