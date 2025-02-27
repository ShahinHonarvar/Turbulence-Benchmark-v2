def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    nums_subset = nums[1:6]
    if len(set(nums_subset)) < 2:
        return None
    return sorted(nums_subset)[1]