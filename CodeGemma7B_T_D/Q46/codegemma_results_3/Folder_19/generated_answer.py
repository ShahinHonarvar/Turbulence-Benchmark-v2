def gcf_three_nums(nums):
    a = nums[40]
    b = nums[15]
    c = nums[99]
    gcd = max(a, min(b, c), key=lambda x: x % min(b, c))
    return gcd