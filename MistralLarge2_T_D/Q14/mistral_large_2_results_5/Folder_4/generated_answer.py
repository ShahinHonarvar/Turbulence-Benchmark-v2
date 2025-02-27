def find_second_smallest_num(nums):
    if len(nums) < 85:
        return None
    subset = sorted(nums[70:85])
    if len(subset) < 2:
        return None
    return subset[1]