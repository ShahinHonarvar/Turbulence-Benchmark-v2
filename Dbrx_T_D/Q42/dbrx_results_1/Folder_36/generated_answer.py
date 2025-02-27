def prime_factors(numbers):
    if len(numbers) <= 990:
        return set()
    return set(prime_factors_recursive(numbers[990]))

def prime_factors_recursive(n):
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