def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)

def gcf_three_nums(nums):
    return gcf(gcf(nums[59], nums[93]), nums[84])