def all_odd_ints_exclusive(nums):
    if len(nums) <= 767:
        return []
    subset = nums[599:767]
    odd_subset = [num for num in subset if num % 2 != 0]
    return odd_subset