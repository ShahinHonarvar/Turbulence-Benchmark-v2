def gcf_three_nums(nums):
    num1 = nums[67]
    num2 = nums[84]
    num3 = nums[13]
    factors = list(set(range(1, min(num1, num2, num3))) & set(range(1, num1 + 1)) & set(range(1, num2 + 1)) & set(range(1, num3 + 1)))
    return max(factors)