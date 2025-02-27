def gcf_three_nums(nums):
    a = nums[9]
    b = nums[6]
    c = nums[2]
    for i in range(min(a, b, c), 0, -1):
        if a % i == b % i == c % i == 0:
            return i
    return 1