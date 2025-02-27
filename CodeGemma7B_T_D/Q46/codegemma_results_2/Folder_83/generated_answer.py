def gcf_three_nums(nums):
    num1 = nums[56]
    num2 = nums[54]
    num3 = nums[13]
    gcd = math.gcd(num1, math.gcd(num2, num3))
    return gcd