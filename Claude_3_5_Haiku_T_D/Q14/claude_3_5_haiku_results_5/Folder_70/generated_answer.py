def find_second_smallest_num(nums):
    if len(nums) < 50:
        return None
    subset = nums[35:50]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]