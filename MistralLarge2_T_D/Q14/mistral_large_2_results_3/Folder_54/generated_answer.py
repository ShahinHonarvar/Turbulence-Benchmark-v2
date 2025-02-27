def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    subset = sorted(nums[68:87])
    if len(subset) < 2:
        return None
    return subset[1]