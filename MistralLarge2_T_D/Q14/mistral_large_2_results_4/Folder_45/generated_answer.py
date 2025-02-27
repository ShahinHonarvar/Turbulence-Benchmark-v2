def find_second_smallest_num(nums):
    subset = nums[30:201]
    unique_sorted = sorted(set(subset))
    return unique_sorted[1] if len(unique_sorted) > 1 else None