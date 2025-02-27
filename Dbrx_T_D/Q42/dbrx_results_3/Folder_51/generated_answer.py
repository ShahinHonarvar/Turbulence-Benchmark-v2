def prime_factors(numbers):
    if len(numbers) <= 64:
        return 'List is too short.'
    num = numbers[64]
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return set(factors)