def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(nums):
    return gcf(gcf(nums[46], nums[84]), nums[23])