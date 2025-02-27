def find_second_smallest_num(nums):
    if not nums or len(nums) < 371:
        return None
    subset = nums[310:371]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]