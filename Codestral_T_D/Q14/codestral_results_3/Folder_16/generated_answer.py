def find_second_smallest_num(nums):
    subset = sorted(nums[66:78])
    if len(subset) > 1:
        return subset[1]
    else:
        return None