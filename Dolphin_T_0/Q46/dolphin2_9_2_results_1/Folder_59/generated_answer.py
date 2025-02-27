def gcf_three_nums(nums):
    a = nums[7]
    b = nums[6]
    c = nums[8]
    for i in range(min(a, b, c), 1, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
    return 1