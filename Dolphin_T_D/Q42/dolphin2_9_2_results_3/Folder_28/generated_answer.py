def prime_factors(numbers):
    num = numbers[37]
    factors = []
    i = 2
    while num > 1:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    return set(factors)