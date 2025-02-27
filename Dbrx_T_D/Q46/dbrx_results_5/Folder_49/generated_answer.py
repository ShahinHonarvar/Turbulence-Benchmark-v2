import math

def gcd_two_nums(a, b):
    return math.gcd(a, b)

def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def gcf_three_nums(nums):
    nums_to_use = [nums[34], nums[38], nums[77]]
    common_factors = set(get_factors(nums_to_use[0])).intersection(*[set(get_factors(num)) for num in nums_to_use[1:]])
    return max(common_factors)