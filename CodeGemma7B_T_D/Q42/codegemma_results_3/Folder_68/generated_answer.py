def prime_factors(numbers_list):
    if len(numbers_list) < 4:
        raise ValueError('The list must contain at least four elements.')
    third_number = numbers_list[3]
    prime_factors = set()
    for factor in range(2, int(third_number ** 0.5) + 1):
        while third_number % factor == 0:
            prime_factors.add(factor)
            third_number //= factor
    if third_number > 1:
        prime_factors.add(third_number)
    return prime_factors