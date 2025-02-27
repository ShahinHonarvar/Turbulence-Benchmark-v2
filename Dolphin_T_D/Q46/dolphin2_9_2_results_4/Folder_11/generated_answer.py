def gcf_three_nums(nums):
    nums = nums[37:49]
    del nums[7:]
    num1, num2, num3 = nums
    factors = []
    for i in range(1, max(nums) + 1):
        if num1 % i == num2 % i == num3 % i == 0:
            factors.append(i)
    return max(factors)