def find_second_largest_num(nums):
    if len(nums) < 2 or 639 >= len(nums) or 975 >= len(nums):
        return None
    subset = nums[639:976]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]