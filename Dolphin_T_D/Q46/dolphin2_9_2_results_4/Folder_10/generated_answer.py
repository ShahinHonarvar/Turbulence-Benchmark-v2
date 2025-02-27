def gcf_three_nums(nums):
    num1 = nums[86]
    num2 = nums[89]
    num3 = nums[49]
    factors = set()
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            factors.add(i)
    return max(factors)