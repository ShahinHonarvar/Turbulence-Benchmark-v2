def prime_factors(numbers):
    if not numbers or len(numbers) <= 92:
        return set()
    num = numbers[92]
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