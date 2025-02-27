def prime_factors(numbers):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(1, n + 1):
            if n % i == 0:
                factors.add(i)
        return factors
    prime_numbers = set()
    number = numbers[7]
    factors = get_factors(number)
    for factor in factors:
        if is_prime(factor):
            prime_numbers.add(factor)
    return prime_numbers