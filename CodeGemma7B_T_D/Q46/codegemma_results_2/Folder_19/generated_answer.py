def gcf_three_nums(nums):
    num1, num2, num3 = (nums[40], nums[15], nums[99])
    return math.gcd(num1, math.gcd(num2, num3))