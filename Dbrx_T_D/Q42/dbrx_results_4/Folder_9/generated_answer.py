def prime_factors(numbers):
    factors = set()
    for num in numbers:
        if num > 2 ** 24:
            raise ValueError('All numbers in the list must be less than or equal to 2^24')
        for potential_factor in range(2, int(num ** 0.5) + 1):
            if num % potential_factor == 0:
                factors.add(potential_factor)
                num //= potential_factor
                while num % potential_factor == 0:
                    num //= potential_factor
        if num > 1:
            factors.add(num)
    return factors