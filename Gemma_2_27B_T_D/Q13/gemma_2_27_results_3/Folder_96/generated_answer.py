def find_second_largest_num(nums):
    nums_subset = nums[15:52]
    if len(nums_subset) < 2:
        return None
    return sorted(nums_subset)[-2]