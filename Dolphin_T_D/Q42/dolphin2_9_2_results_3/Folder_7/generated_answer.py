def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors_set = set()
    for factor in numbers[851]:
        if is_prime(factor):
            prime_factors_set.add(factor)
    return prime_factors_set