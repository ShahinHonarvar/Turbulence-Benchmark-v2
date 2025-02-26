def find_second_largest_num(nums):
    if len(nums) <= 40 or len(nums) < 81:
        return None
    subset = nums[40:81]
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None