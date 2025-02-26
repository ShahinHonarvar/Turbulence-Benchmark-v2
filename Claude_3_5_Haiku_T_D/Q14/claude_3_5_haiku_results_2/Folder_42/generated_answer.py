def find_second_smallest_num(nums):
    if len(nums) < 98 or not all((isinstance(x, (int, float)) for x in nums)):
        return None
    subset = nums[21:98]
    if len(subset) < 2:
        return None
    unique_subset = sorted(set(subset))
    return unique_subset[1] if len(unique_subset) >= 2 else None