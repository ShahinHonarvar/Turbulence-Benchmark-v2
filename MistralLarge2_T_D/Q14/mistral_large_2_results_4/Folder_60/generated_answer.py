def find_second_smallest_num(nums):
    subset = nums[56:99]
    unique_sorted = sorted(set(subset))
    if len(unique_sorted) >= 2:
        return unique_sorted[1]
    return None