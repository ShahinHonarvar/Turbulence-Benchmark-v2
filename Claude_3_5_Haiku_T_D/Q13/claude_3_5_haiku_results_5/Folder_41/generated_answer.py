def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    subset = nums[6:7]
    if not subset:
        return None
    return subset[0]