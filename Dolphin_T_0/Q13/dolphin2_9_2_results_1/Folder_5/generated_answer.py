def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    subset = nums[8:10]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1]