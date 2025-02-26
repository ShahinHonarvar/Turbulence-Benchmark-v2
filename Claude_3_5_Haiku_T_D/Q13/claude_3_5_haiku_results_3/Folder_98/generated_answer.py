def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 7:
        return None
    subset = nums[:7]
    subset.sort(reverse=True)
    return subset[1] if len(set(subset)) > 1 else None