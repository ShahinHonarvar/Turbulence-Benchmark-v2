def gcf(a, b):
    if a % b == 0:
        return b
    return gcf(b, a % b)

def gcf_three_nums(nums):
    return gcf(gcf(nums[47], nums[10]), nums[28])