def find_second_smallest_num(nums):
    if len(nums) < 69:
        return None
    subset = nums[42:69]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]