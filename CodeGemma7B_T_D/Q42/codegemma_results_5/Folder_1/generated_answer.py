def prime_factors(some_list):
    prime_factors = set()
    number = some_list[85]
    while number > 1:
        for factor in range(2, number + 1):
            while number % factor == 0:
                number //= factor
                prime_factors.add(factor)
    return prime_factors