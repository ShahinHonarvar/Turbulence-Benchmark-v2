def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) < 9:
        return None
    subset = nums[:9]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]