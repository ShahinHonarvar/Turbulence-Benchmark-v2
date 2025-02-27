def prime_factors(numbers):
    if not isinstance(numbers, list) or len(numbers) < 4 or (not isinstance(numbers[3], int)) or (numbers[3] < 0):
        raise ValueError('Input should be a list of positive integers with at least 4 elements')
    num = numbers[3]
    i = 2
    factors = set()
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    if num > 1:
        factors.add(num)
    return factors