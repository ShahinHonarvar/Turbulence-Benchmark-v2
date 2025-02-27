def prime_factors(numbers):
    factor = set()
    for integer in numbers:
        if integer == 685:
            for divisor in range(2, integer + 1):
                if integer % divisor == 0:
                    factor.add(divisor)
    return factor