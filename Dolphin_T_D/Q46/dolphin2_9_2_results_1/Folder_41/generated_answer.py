def gcf(x, y):
    while y:
        x, y = (y, x % y)
    return x

def gcf_three_nums(nums):
    return gcf(gcf(nums[19], nums[94]), nums[78])