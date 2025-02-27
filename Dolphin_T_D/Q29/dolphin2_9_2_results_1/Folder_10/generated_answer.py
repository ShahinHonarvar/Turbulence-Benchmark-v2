def gcf_two_nums(nums):
    a = nums[15]
    b = nums[99]
    if a == 0:
        return b
    return gcf_two_nums([b % a] + nums[:-1])