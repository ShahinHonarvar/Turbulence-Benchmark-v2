from sympy import isprime

def find_primes_between_indices(lst):
    primes = [num for num in lst[22:51] if isprime(num)]
    primes.sort(reverse=True)
    return primes