def find_second_largest_num(nums):
    if len(nums) < 98:
        return None
    subset = nums[21:98]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    return max(subset) if subset else None