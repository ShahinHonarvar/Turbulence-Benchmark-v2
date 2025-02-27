def gcf_three_nums(nums):
    a, b, c = (nums[693], nums[331], nums[668])
    gcd = a
    if b % gcd == 0 and c % gcd == 0:
        return gcd
    while b % gcd != 0 or c % gcd != 0:
        gcd -= 1
    return gcd