def find_second_largest_num(nums):
    if len(nums) < 747:
        return None
    subset = nums[262:747]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]