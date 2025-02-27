def gcf_three_nums(nums):
    a = nums[96]
    b = nums[53]
    c = nums[35]
    return math.gcd(a, math.gcd(b, c))