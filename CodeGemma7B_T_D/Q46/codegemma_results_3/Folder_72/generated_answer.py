def gcf_three_nums(nums):
    x, y, z = (nums[44], nums[91], nums[42])
    return math.gcd(x, math.gcd(y, z))