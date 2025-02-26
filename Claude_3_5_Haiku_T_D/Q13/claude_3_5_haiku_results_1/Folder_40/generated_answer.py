def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    subset = nums[:3]
    subset.sort(reverse=True)
    if len(subset) >= 2:
        return subset[1]
    return None