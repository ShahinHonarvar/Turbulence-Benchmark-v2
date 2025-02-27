def prime_factors(numbers):

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target = numbers[6]
    factors = []
    for i in range(1, target + 1):
        if is_prime(i) and target % i == 0:
            factors.append(i)
    return set(factors)