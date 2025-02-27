def gcf_two_nums(nums):
    a = nums[0]
    b = nums[1]
    if a == 0:
        return b
    return gcf_two_nums([b % a, a])