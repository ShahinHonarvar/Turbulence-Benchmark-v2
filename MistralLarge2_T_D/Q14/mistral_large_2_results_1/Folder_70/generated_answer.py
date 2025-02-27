def find_second_smallest_num(nums):
    if len(nums) < 50:
        return None
    subset = sorted(nums[35:50])
    if len(subset) < 2:
        return None
    return subset[1]