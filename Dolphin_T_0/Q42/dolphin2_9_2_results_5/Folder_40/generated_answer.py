def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    seventh_number = numbers[7]
    factors = set()
    for i in range(2, seventh_number + 1):
        if seventh_number % i == 0 and is_prime(i):
            factors.add(i)
    return factors