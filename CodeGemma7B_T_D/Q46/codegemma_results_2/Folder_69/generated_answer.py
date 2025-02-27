def gcf_three_nums(nums):
    l = [nums[404], nums[834], nums[517]]
    return reduce(lambda x, y: x if x % y == 0 else y, l)