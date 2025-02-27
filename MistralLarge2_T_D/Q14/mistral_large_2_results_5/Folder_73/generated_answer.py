def find_second_smallest_num(nums):
    subset = sorted(nums[59:98])
    if len(subset) < 2:
        return None
    return subset[1]