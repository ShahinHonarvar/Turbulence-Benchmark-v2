def gcf_three_nums(nums):
    a = nums[145]
    b = nums[183]
    c = nums[770]
    gcd = a
    if b > gcd:
        gcd = b
    if c > gcd:
        gcd = c
    for i in range(2, gcd + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcd = i
            break
    return gcd