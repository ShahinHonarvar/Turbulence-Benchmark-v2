import sympy

def all_left_right_truncatable_prime(nums):
    x = nums[49]
    primes = [p for p in sympy.primerange(2, x + 1) if '0' not in str(p)]
    return sorted([p for p in primes if all((int(str(p)[i:]) in primes and int(str(p)[:-i]) in primes for i in range(1, len(str(p)))))])