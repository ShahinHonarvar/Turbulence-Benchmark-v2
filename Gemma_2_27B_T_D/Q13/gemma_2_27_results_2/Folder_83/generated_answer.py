def find_second_largest_num(nums):
    if len(nums) < 2 or 90 not in range(len(nums)):
        return None
    nums_subset = nums[90:91]
    if len(nums_subset) < 2:
        return None
    return sorted(nums_subset)[-2]