def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    index_990 = numbers[990]
    factors = set()
    for i in range(2, index_990 + 1):
        if index_990 % i == 0 and is_prime(i):
            factors.add(i)
    return factors