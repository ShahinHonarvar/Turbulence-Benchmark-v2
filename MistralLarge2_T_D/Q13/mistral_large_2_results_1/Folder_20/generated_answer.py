def find_second_largest_num(nums):
    subset = nums[56:67]
    if len(subset) < 2:
        return None
    unique_sorted = sorted(set(subset), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None