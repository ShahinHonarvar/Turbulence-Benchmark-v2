def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(nums):
    if len(nums) < 100:
        return None
    else:
        return gcf(gcf(nums[99], nums[63]), nums[74])