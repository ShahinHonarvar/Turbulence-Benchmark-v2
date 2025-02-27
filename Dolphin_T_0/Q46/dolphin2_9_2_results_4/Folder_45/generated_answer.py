def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)

def gcf_three_nums(nums):
    return gcf(gcf(nums[46], nums[84]), nums[23])