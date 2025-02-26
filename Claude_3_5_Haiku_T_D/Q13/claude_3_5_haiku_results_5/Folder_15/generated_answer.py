def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    subset = nums[0:4]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]