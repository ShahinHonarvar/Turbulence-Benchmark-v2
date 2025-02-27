from sympy import isprime

def find_primes_between_indices(lst):
    primes = [i for i in lst[72:73] if isprime(i)]
    primes.sort()
    return primes