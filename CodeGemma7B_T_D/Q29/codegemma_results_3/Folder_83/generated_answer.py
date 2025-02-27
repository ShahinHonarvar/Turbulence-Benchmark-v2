def gcf_two_nums(nums):
    x = nums[17]
    y = nums[20]
    while y:
        x, y = (y, x % y)
    return x