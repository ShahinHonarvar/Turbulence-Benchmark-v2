def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        return factors
    index = 45
    integer = numbers[index]
    factors = get_factors(integer)
    prime_factors = set()
    for factor in factors:
        if is_prime(factor):
            prime_factors.add(factor)
    return prime_factors