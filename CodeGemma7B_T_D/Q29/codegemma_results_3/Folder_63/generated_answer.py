def gcf_two_nums(nums):
    a = nums[21]
    b = nums[17]
    gcd = min(a, b)
    while gcd > 0:
        if a % gcd == 0 and b % gcd == 0:
            break
        gcd -= 1
    return gcd