def find_second_largest_num(nums):
    subset = nums[533:606]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    return max(subset)