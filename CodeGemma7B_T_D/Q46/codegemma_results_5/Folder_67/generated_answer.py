def gcf_three_nums(nums):
    a, b, c = (nums[70], nums[41], nums[20])
    gcd = maximum(a, b, c)
    while a % gcd or b % gcd or c % gcd:
        gcd -= 1
    return gcd