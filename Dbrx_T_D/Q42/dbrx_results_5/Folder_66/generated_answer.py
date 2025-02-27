def prime_factors(numbers):
    if 42 not in range(len(numbers)):
        raise IndexError('Index 42 is out of range')
    n = numbers[42]
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