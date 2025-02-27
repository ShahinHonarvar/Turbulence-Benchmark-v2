def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 774:
        return None
    subset = nums[667:775]
    if len(set(subset)) < 2:
        return None
    else:
        subset.sort(reverse=True)
        return subset[1]