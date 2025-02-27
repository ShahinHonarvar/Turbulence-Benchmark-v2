def prime_factors(numbers):
    num = numbers[47]
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    i = 3
    while i * i <= num:
        if num % i == 0:
            factors.add(i)
            num //= i
        else:
            i += 2
    if num > 1:
        factors.add(num)
    return factors