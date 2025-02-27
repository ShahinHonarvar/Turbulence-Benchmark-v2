def prime_factors(numbers):
    target = numbers[312]
    i = 2
    factors = set()
    while i * i <= target:
        if target % i:
            i += 1
        else:
            target //= i
            factors.add(i)
    if target > 1:
        factors.add(target)
    return factors