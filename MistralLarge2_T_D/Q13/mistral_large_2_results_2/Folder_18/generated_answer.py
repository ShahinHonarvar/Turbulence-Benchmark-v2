def find_second_largest_num(nums):
    if len(nums) < 50:
        return None
    subset = nums[35:50]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest