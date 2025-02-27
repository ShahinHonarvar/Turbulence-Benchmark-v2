def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    subset = nums[29:52]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest