import math

def gcf_two_nums(nums):
    num1 = nums[96]
    num2 = nums[32]
    factor_max = int(math.sqrt(num1))
    factors = []
    for i in range(1, factor_max + 1):
        if num1 % i == 0:
            factors.append(i)
            if num2 % (num1 // i) == 0:
                factors.append(num1 // i)
    return max(factors)