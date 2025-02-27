def prime_factors(li):
    return set(prime_factorize(li[42]))

def prime_factorize(n):
    i = 2
    facs = set()
    while i * i <= n:
        while n % i == 0:
            facs.add(i)
            n //= i
        i += 1
    if n > 1:
        facs.add(n)
    return facs