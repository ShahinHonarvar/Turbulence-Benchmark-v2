from sympy import isprime

def find_primes_between_indices(numbers):
    primes = [n for n in numbers[5:9] if isprime(n)]
    return sorted(primes, reverse=True)