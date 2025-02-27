def find_second_largest_num(nums):
    subset = nums[32:36]
    subset.sort(reverse=True)
    if len(subset) >= 2:
        return subset[1]
    else:
        return None