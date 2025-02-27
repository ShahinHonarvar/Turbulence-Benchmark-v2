from math import sqrt

def prime_factors(nums):
    i = 23
    factors = set()
    for num in range(2, int(sqrt(nums[i])) + 1):
        while nums[i] % num == 0:
            factors.add(num)
            nums[i] //= num
    if nums[i] != 1:
        factors.add(nums[i])
    return factors