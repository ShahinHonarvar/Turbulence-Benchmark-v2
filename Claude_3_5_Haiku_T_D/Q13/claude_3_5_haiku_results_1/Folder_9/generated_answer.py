def find_second_largest_num(nums):
    if len(nums) <= 200:
        return None
    subset = nums[200:201]
    if not subset:
        return None
    return subset[0]