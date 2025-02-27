def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factors(num):
        factor_set = set()
        for i in range(2, num + 1):
            while num % i == 0:
                factor_set.add(i)
                num //= i
        return factor_set
    target_number = numbers[4]
    return {factor for factor in factors(target_number) if is_prime(factor)}