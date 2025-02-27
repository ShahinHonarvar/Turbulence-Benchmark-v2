def find_second_largest_num(nums):
    if len(nums) < 775:
        return None
    subset = nums[667:775]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    return max(subset)