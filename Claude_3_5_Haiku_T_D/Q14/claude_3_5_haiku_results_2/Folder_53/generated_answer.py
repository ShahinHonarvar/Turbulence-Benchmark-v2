def find_second_smallest_num(nums):
    if len(nums) <= 1 or len(nums) < 102:
        return None
    subset = nums[1:101]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1] if len(sorted_subset) > 1 else None