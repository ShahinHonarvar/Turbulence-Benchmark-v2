def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    subset = nums[1:6]
    if len(set(subset)) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]