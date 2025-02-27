def find_second_smallest_num(nums):
    nums_subset = sorted(nums[43:87])
    if len(nums_subset) < 2:
        return None
    else:
        return nums_subset[1]