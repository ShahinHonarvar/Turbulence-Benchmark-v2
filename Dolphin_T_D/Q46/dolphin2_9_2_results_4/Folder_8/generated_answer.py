def gcf(a, b):
    while b != 0:
        a %= b
        a, b = (b, a)
    return a

def gcf_three_nums(nums):
    return gcf(gcf(nums[99], nums[28]), nums[53])