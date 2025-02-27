from sympy import isprime

def find_primes_between_indices(prime_list):
    primes = []
    for i in range(40, 69):
        if isprime(prime_list[i]):
            primes.append(prime_list[i])
    if not primes:
        return []
    return sorted(primes, reverse=True)