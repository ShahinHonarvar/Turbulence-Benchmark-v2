def find_second_largest_num(nums):
    subset = nums[80:201]
    if len(subset) < 2:
        return None
    first_max = max(subset)
    subset.remove(first_max)
    return max(subset) if subset else None