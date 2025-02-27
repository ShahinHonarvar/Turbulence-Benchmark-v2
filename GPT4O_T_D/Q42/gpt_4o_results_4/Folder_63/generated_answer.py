def prime_factors(lst):
    if len(lst) <= 57:
        return set()
    num = lst[57]
    primes = set()
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            primes.add(divisor)
            num //= divisor
        divisor += 1
    return primes