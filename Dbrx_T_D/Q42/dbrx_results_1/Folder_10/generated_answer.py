def prime_factors(numbers):
    return {factor for number in numbers[54:55] for factor in get_prime_factors(number)}

def get_prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors