def find_second_largest_num(nums):
    if len(nums) < 51:
        return None
    subset = nums[22:51]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    return max(subset)