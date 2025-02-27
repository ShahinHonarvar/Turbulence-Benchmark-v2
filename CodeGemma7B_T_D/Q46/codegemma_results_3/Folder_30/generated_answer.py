def gcf_three_nums(nums):
    a, b, c = (nums[76], nums[35], nums[74])
    return math.gcd(a, math.gcd(b, c))