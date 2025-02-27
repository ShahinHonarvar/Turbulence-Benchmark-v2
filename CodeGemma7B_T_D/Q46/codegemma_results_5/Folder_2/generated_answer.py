def gcf_three_nums(nums):
    num1, num2, num3 = (nums[307], nums[920], nums[463])
    return reduce(gcd, [num1, num2, num3])