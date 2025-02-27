def gcf_three_nums(nums):
    num1 = nums[66]
    num2 = nums[56]
    num3 = nums[92]
    gcd = GCD(num1, num2)
    return GCD(gcd, num3)