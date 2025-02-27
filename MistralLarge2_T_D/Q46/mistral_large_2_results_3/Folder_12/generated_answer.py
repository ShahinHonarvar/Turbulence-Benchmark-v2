def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcf(gcf(nums[91], nums[45]), nums[48])