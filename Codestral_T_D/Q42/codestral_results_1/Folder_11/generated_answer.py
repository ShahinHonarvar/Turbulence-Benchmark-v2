def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    number = numbers[77]
    factors = set()
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            number //= factor
            factors.add(factor)
        elif is_prime(factor):
            factor += 1
        else:
            factor += 2
    if number > 1:
        factors.add(number)
    return factors