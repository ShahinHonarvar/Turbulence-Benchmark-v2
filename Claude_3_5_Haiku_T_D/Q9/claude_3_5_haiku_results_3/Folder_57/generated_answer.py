def all_odd_ints_inclusive(nums):
    if len(nums) <= 55:
        return []
    subset = nums[27:56]
    return [num for num in subset if num % 2 != 0]