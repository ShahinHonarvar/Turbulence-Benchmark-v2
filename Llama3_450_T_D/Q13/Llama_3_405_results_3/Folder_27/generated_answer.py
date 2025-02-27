def find_second_largest_num(nums):
    if len(nums) < 67 or len(nums) < 94:
        return None
    nums_subset = nums[66:94]
    if len(nums_subset) < 2:
        return None
    nums_subset.sort(reverse=True)
    return nums_subset[1]