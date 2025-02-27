def find_second_largest_num(nums):
    subset = nums[36:77]
    if len(set(subset)) < 2:
        return None
    else:
        sorted_subset = sorted(set(subset), reverse=True)
        return sorted_subset[1]