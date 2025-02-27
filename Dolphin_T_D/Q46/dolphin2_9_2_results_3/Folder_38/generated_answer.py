def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)

def gcf_three_nums(nums):
    return gcf(gcf(nums[14], nums[21]), nums[17])