import sympy

def find_primes_between_indices(nums):
    return sorted([n for i, n in enumerate(nums[76:93], 76) if sympy.isprime(n)])