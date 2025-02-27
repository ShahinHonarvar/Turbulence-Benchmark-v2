def gcf_three_nums(nums):
    a = nums[25]
    b = nums[76]
    c = nums[57]
    g = math.gcd(a, b)
    return math.gcd(g, c)