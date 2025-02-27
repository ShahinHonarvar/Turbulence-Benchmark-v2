def prime_factors(numbers):
    prime_factors_90 = set()
    for num in numbers:
        if num > 90:
            continue
        factor = 2
        while num % factor != 0:
            factor += 1
        while num % factor == 0:
            prime_factors_90.add(factor)
            num //= factor
    return prime_factors_90