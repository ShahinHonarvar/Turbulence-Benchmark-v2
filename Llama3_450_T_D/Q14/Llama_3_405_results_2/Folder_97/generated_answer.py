def find_second_smallest_num(nums):
    if len(nums) < 35:
        return None
    subset = nums[31:35]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]