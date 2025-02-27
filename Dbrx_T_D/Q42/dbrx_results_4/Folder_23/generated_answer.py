def prime_factors(numbers):
    if not isinstance(numbers, list) or len(numbers) <= 69:
        return set()
    num = numbers[69]
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