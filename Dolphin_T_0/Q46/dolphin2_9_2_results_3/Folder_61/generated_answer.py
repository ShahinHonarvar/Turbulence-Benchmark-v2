def gcf_three_nums(nums):
    a = nums[1]
    b = nums[2]
    c = nums[7]
    gcd = 1
    for i in range(2, min(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            gcd = i
    return gcd