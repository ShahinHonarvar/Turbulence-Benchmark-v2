def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcf(nums[74], gcf(nums[60], nums[28]))