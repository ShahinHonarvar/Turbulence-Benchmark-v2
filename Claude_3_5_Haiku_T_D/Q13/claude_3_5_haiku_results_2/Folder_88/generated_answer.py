def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    subset = nums[4:9]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]