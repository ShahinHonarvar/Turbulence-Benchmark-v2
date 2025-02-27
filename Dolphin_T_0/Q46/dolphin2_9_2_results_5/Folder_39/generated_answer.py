def gcf_three_nums(nums):
    num1 = nums[85]
    num2 = nums[36]
    num3 = nums[54]
    factors = []
    for factor in range(1, max(num1, num2, num3) + 1):
        if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0):
            factors.append(factor)
    return max(factors)