def find_second_largest_num(nums):
    if not nums or len(nums) < 94:
        return None
    subset = nums[66:94]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest