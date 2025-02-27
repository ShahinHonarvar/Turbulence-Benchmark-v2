def gcf_three_nums(nums):
    num1 = nums[4]
    num2 = nums[0]
    num3 = nums[8]
    return math.gcd(num1, math.gcd(num2, num3))