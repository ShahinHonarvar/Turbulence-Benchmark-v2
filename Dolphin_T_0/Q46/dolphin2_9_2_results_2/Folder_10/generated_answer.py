def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(nums):
    return gcf(gcf(nums[86], nums[89]), nums[49])