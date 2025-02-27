def prime_factors(numbers):
    if len(numbers) < 16:
        raise IndexError('List must have at least 16 elements')
    num = numbers[15]
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