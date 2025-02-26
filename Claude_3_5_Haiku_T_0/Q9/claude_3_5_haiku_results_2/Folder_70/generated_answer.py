def all_odd_ints_inclusive(nums):
    if len(nums) < 33:
        return []
    subset = nums[28:33]
    return [num for num in subset if num % 2 != 0]