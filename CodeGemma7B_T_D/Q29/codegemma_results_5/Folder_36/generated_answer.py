def gcf_two_nums(nums):
    a = nums[429]
    b = nums[289]
    gcd = None
    i = 2
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcd = i
        i += 1
    return gcd