def all_odd_ints_exclusive(nums):
    subset = nums[81:86]
    odd_ints = [i for i in subset if i % 2 != 0]
    return odd_ints