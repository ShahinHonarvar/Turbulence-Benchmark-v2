def prime_factors(numbers):
    factor_set = set()
    number = numbers[94]
    while number % 2 == 0:
        number //= 2
        factor_set.add(2)
    for i in range(3, int(number ** 0.5) + 1, 2):
        while number % i == 0:
            number //= i
            factor_set.add(i)
    if number > 1:
        factor_set.add(number)
    return factor_set