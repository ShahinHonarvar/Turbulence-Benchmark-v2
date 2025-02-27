def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    index69 = numbers[69]
    factors = set()
    for i in range(2, index69 + 1):
        if is_prime(i) and index69 % i == 0:
            factors.add(i)
    return factors