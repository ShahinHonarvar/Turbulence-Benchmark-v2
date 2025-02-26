def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    subset = nums[0:3]
    subset.sort(reverse=True)
    if len(subset) < 2:
        return None
    return subset[1]