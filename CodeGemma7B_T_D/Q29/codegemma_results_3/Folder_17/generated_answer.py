def gcf_two_nums(nums):
    return gcf(nums[69], nums[40])

def gcf(a, b):
    return a if b == 0 else gcf(b, a % b)