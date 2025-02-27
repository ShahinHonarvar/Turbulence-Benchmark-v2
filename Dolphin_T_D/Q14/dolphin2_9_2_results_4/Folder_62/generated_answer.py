def find_second_smallest_num(nums):
    subset = nums[10:67]
    if len(subset) < 2:
        return None
    subset.sort()
    if subset[1] == subset[0]:
        return None
    return subset[1]