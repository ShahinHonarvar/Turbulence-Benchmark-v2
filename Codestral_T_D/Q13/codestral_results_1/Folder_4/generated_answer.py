def find_second_largest_num(nums):
    subset = sorted(nums[12:93], reverse=True)
    if len(subset) < 2:
        return None
    else:
        return subset[1]