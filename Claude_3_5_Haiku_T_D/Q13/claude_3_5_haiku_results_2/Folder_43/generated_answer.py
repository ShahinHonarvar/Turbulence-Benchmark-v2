def find_second_largest_num(nums):
    if len(nums) < 87 or len(nums[68:87]) < 2:
        return None
    subset = nums[68:87]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]