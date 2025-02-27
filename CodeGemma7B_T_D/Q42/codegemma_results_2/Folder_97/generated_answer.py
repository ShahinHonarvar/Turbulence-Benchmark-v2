def prime_factors(numbers):
    try:
        number = numbers[132]
    except IndexError:
        raise ValueError('Index 132 does not exist in the list.')
    factors = set()
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            factors.add(i)
            number //= i
    if number > 1:
        raise ValueError('Cannot find prime factors of a number greater than 1.')
    return factors