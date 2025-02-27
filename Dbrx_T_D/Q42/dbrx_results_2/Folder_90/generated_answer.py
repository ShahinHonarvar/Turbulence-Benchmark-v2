def prime_factors(numbers):
    if len(numbers) <= 263:
        return 'Index out of range. List should have more than 263 elements.'
    num = numbers[263]
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