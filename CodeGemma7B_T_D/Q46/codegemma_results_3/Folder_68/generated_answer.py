def gcf_three_nums(nums):
    a, b, c = (nums[4], nums[1], nums[7])
    return gcf(a, gcf(b, c))

def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a