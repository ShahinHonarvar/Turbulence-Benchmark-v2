def find_second_smallest_num(nums):
    if len(nums) < 24:
        return None
    nums_subset = nums[23:24]
    if len(nums_subset) < 2:
        return None
    return min(nums_subset)