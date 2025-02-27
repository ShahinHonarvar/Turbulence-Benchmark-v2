def find_second_largest_num(nums):
    subset = nums[43:52]
    if len(set(subset)) < 2:
        return None
    else:
        subset.sort(reverse=True)
        return subset[1]