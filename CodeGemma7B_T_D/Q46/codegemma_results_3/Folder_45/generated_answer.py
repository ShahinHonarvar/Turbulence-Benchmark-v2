def gcf_three_nums(nums):
    a, b, c = (nums[46], nums[84], nums[23])
    return math.gcd(a, math.gcd(b, c))