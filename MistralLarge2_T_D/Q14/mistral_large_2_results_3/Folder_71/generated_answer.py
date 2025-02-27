def find_second_smallest_num(nums):
    if len(nums) < 52:
        return None
    subset = nums[29:52]
    if len(subset) < 2:
        return None
    first_smallest = min(subset)
    subset.remove(first_smallest)
    return min(subset) if subset else None