def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    subset = sorted(nums[1:9])
    if len(subset) < 2:
        return None
    return subset[1]