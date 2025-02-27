def prime_factors(numbers):
    if len(numbers) <= 56:
        return set()
    prime_factors = set()
    n = numbers[56]
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.add(i)
    if n > 1:
        prime_factors.add(n)
    return prime_factors