def prime_factors(numeros):
    prime_factors = set()
    number = numeros[94]
    i = 2
    while i <= number:
        if number % i:
            i += 1
        else:
            prime_factors.add(i)
            number //= i
    return prime_factors