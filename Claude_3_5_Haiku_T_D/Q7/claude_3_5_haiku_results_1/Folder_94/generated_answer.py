def all_even_ints_inclusive(nums):
    if len(nums) <= 40:
        return []
    subset = nums[28:41]
    return [num for num in subset if num % 2 == 0]