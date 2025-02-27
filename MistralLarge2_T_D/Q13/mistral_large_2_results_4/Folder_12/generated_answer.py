def find_second_largest_num(nums):
    if len(nums) < 65:
        return None
    subset = nums[14:65]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest