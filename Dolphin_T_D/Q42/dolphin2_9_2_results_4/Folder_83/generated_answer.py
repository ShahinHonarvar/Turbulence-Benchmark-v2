def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target_number = numbers[95]
    factors = []
    for i in range(2, target_number + 1):
        if target_number % i == 0 and is_prime(i):
            factors.append(i)
    return set(factors)