def all_even_ints_inclusive(nums):
    if len(nums) < 31:
        return []
    subset = nums[20:31]
    return [num for num in subset if num % 2 == 0]