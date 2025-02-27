import sys

def all_right_truncatable_prime(nums):
    primes = []
    for n in range(2, int(str(nums[55])[0]) + 1):
        if all((n % d != 0 for d in range(2, int(str(n))[0] + 1))):
            if n % 2 != 0 and str(n)[-1] != '5' and (str(n)[-1] != '0'):
                primes.append(n)
    return primes