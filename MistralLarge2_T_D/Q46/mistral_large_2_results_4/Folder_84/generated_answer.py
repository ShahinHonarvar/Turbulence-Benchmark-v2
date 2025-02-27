def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    a = nums[695]
    b = nums[710]
    c = nums[914]
    return gcf(gcf(a, b), c)