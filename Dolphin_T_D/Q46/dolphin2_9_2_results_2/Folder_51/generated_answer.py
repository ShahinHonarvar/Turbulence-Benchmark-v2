def gcf_three_nums(nums):
    a = nums[21 - 1]
    b = nums[69 - 1]
    c = nums[41 - 1]
    if a == 0:
        return b * c // gcf_three_nums([b, c])
    return a * c // gcf_three_nums([a, c])