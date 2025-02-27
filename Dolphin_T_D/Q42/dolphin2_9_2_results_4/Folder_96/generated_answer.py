def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_factors(num):
        factors = set()
        for i in range(1, num + 1):
            if num % i == 0:
                factors.add(i)
        return factors
    target_number = numbers[47]
    prime_factors_set = set()
    for factor in get_factors(target_number):
        if is_prime(factor):
            prime_factors_set.add(factor)
    return prime_factors_set