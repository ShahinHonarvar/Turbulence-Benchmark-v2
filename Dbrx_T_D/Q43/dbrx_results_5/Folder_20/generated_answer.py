from sympy import isprime

def find_primes_between_indices(numbers):
    primes = sorted((num for num in numbers[36:41] if isprime(num)), reverse=True)
    return primes