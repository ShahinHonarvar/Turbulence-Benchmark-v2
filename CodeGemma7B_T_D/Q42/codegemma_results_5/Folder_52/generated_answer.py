def prime_factors(numbers):
    for number in numbers:
        if number == numbers[478]:
            for divisor in range(2, number + 1):
                if number % divisor == 0:
                    factors = set()
                    while number % divisor == 0:
                        factors.add(divisor)
                        number //= divisor
                    return factors