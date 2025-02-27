from sympy import isprime

def find_primes_between_indices(lst):
    primes = [num for i, num in enumerate(lst) if 24 <= i <= 32 and isprime(num)]
    return sorted(primes, reverse=True)