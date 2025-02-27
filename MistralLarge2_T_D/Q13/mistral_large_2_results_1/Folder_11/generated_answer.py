def find_second_largest_num(nums):
    if len(nums) <= 51:
        return None
    subset = nums[37:52]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest