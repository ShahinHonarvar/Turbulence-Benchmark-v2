def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    number_to_factorize = numbers[27]
    i = 2
    while i * i <= number_to_factorize:
        if number_to_factorize % i:
            i += 1
        else:
            number_to_factorize //= i
            factors.add(i)
    if number_to_factorize > 1:
        factors.add(number_to_factorize)
    return {i for i in factors if is_prime(i)}