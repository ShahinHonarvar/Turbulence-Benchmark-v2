def prime_factors(positive_int_list):
    factors = set()
    number = positive_int_list[18]
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors