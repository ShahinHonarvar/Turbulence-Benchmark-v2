def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(nums):
    return gcf(nums[56], gcf(nums[54], nums[13]))