def gcf_two_nums(nums):
    a = nums[184]
    b = nums[307]
    if a == 0:
        return b
    return gcf_two_nums([b % a, a])