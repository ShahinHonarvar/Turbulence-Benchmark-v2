def find_second_largest_num(nums):
    if len(nums) <= 746:
        return None
    subset = nums[262:747]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest