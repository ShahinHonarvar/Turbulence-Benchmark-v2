def find_second_largest_num(nums):
    if len(nums) <= 90:
        return None
    subset = nums[90:91]
    if len(subset) == 0:
        return None
    subset.sort(reverse=True)
    return subset[1] if len(subset) > 1 else None