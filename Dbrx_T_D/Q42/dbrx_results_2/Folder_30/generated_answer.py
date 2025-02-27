def prime_factors(numbers):
    return set(prime_factors_for_number(numbers[93]))

def prime_factors_for_number(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors