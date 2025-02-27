def prime_factors(n):
    primes = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            primes.add(i)
    if n > 1:
        primes.add(n)
    return primes

def prime_factors_at_index_321(lst):
    n = lst[321]
    return prime_factors(n)