def find_second_largest_num(nums):
    if len(nums) < 37:
        return None
    subset = nums[35:50]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    return max(subset) if subset else None