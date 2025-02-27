def gcf_three_nums(nums):
    if len(nums) < 75:
        return None
    num1 = nums[19]
    num2 = nums[49]
    num3 = nums[74]
    factors = []
    for i in range(1, max(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.append(i)
    return max(factors)