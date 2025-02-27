def gcf_three_nums(nums):
    a, b, c = (nums[4], nums[1], nums[7])
    gcd = 0
    while b and c:
        if b % a == 0 and c % a == 0:
            gcd = a
        a, b, c = (b % a, c % a, gcd)
    return gcd