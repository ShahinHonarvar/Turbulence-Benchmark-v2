def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    subset = nums[43:52]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]