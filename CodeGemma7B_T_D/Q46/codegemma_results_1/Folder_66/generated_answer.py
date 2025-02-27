def gcf_three_nums(nums):
    a, b, c = (nums[92], nums[69], nums[95])
    gcd = math.gcd(a, b)
    return math.gcd(gcd, c)