def prime_factors(numbers):
    if not isinstance(numbers, list) or len(numbers) <= 23:
        return None
    num = numbers[23]
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