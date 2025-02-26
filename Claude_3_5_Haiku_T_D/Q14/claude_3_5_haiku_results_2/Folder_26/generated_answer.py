def find_second_smallest_num(nums):
    if not nums or len(nums) < 64:
        return None
    subset = nums[62:79]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]