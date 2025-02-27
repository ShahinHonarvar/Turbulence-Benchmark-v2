def prime_factors(numbers):
    n = numbers[60]
    factors = set()
    i = 2
    while n > 1:
        if n % i == 0:
            factors.add(i)
            n = n // i
        else:
            i += 1
    return factors