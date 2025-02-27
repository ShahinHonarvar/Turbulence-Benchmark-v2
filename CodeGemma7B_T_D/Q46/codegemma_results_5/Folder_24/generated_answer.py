def gcf_three_nums(nums):
    a, b, c = (nums[18 - 1], nums[37 - 1], nums[43 - 1])
    return math.gcd(a, math.gcd(b, c))