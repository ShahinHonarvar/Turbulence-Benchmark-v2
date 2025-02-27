def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcf(gcf(nums[13], nums[70]), nums[32])