def gcf_three_nums(nums):
    num1 = nums[21]
    num2 = nums[51]
    num3 = nums[33]
    return math.gcd(num1, math.gcd(num2, num3))