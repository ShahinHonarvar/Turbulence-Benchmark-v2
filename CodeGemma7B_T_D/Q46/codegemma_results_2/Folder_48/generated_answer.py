def gcf_three_nums(nums):
    num1 = nums[654]
    num2 = nums[312]
    num3 = nums[441]
    return math.gcd(num1, math.gcd(num2, num3))