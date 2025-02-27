def find_second_largest_num(nums):
    if len(nums) < 60:
        return None
    subset = nums[25:60]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    return max(subset)