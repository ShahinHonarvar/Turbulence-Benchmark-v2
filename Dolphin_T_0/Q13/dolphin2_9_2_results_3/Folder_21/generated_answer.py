def find_second_largest_num(nums):
    subset = nums[639:976]
    if len(set(subset)) < 2:
        return None
    else:
        first_max = max(subset)
        subset.remove(first_max)
        second_max = max(subset)
        return second_max