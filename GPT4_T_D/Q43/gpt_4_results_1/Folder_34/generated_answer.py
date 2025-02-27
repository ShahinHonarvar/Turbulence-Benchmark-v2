from sympy import isprime

def find_primes_between_indices(numbers):
    result = [num for num in numbers[56:58] if isprime(num)]
    result.sort(reverse=True)
    return result