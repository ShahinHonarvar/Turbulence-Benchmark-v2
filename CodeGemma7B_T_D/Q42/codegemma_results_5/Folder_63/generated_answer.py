from math import sqrt

def prime_factors(nums):
    prime_factors = set()
    for f in range(2, int(sqrt(nums[57])) + 1):
        while nums[57] % f == 0:
            prime_factors.add(f)
            nums[57] /= f
    if nums[57] > 1:
        prime_factors.add(int(nums[57]))
    return prime_factors