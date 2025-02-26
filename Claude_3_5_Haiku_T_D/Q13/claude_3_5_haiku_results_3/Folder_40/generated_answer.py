def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    subset = nums[0:3]
    subset.sort(reverse=True)
    return subset[1] if len(subset) > 1 else None