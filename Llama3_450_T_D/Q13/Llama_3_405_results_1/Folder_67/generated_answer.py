def find_second_largest_num(nums):
    nums_subset = nums[22:51]
    if len(nums_subset) < 2:
        return None
    nums_subset.sort(reverse=True)
    return nums_subset[1]