def find_second_largest_num(nums):
    if len(nums) < 84 or len(nums[82:87]) < 2:
        return None
    subset = nums[82:87]
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None