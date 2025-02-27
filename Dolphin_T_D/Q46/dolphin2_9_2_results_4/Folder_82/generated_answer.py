def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcf(gcf(nums[67], nums[84]), nums[13])