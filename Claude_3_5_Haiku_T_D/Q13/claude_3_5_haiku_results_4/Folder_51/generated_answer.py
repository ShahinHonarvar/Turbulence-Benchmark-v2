def find_second_largest_num(nums):
    if not nums or len(nums) < 9:
        return None
    subset = nums[1:9]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1]