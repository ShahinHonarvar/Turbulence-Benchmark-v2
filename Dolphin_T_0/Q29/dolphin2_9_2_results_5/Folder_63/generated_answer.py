def gcf_two_nums(nums):
    a = nums[21]
    b = nums[17]
    for i in range(min(a, b), 1, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1