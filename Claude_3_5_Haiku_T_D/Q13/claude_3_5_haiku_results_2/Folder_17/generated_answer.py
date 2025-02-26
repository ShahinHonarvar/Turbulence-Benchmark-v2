def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    subset = nums[62:79]
    if len(subset) < 2:
        return None
    unique_sorted = sorted(set(subset), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None