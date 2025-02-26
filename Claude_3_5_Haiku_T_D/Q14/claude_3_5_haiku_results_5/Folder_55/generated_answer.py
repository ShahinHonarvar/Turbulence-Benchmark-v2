def find_second_smallest_num(nums):
    if len(nums) < 11:
        return None
    subset = nums[10:11]
    if not subset:
        return None
    return subset[0]