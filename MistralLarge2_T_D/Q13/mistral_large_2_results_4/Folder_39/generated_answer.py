def find_second_largest_num(nums):
    if len(nums) < 31:
        return None
    subset = nums[20:31]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]