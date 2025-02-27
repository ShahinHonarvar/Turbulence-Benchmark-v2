def gcf_three_nums(nums):
    a, b, c = (nums[19], nums[69], nums[97])
    for i in range(min(a, b, c), 0, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
    return 1