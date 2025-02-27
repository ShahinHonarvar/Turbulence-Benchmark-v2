def find_second_largest_num(nums):
    if len(nums) < 60:
        return None
    subset = nums[25:60]
    if len(subset) < 2:
        return None
    max1 = max(subset)
    subset.remove(max1)
    max2 = max(subset)
    return max2