def find_second_smallest_num(nums):
    subset = nums[31:35]
    if len(subset) < 2:
        return None
    subset = sorted(subset)
    return subset[1]