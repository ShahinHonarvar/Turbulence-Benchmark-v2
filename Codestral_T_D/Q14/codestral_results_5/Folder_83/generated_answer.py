def find_second_smallest_num(nums):
    subset = sorted(nums[90:201])
    if len(subset) < 2:
        return None
    else:
        return subset[1]