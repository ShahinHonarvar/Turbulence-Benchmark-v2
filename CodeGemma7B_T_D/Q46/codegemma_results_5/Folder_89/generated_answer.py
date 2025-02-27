def gcf_three_nums(nums):
    num1 = nums[63]
    num2 = nums[73]
    num3 = nums[11]
    return math.gcd(num1, math.gcd(num2, num3))