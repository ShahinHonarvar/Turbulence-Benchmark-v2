def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    index_410 = numbers[410]
    factors = set()
    for i in range(2, index_410 + 1):
        if is_prime(i) and index_410 % i == 0:
            factors.add(i)
    return factors