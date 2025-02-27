def prime_factors(integer):
    factors = set()
    i = 2
    while i * i <= integer:
        if integer % i:
            i += 1
        else:
            integer //= i
            factors.add(i)
    if integer > 1:
        factors.add(integer)
    return factors