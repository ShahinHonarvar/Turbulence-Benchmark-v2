def gcf_two_nums(nums):
    return greatest_common_factor(nums[96], nums[32])

def greatest_common_factor(a, b):
    return a if b == 0 else greatest_common_factor(b, a % b)