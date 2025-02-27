def gcf_two_nums(nums):
    x = nums[95]
    y = nums[73]
    while y:
        x, y = (y, x % y)
    return x