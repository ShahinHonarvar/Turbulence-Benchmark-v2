def gcf_three_nums(nums):
    a, b, c = (nums[95], nums[52], nums[34])
    return gcf(a, gcf(b, c))