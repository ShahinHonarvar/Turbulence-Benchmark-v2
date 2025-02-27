def find_second_largest_num(nums):
    subset = sorted(nums[:4], reverse=True)
    return subset[1] if len(subset) > 1 else None