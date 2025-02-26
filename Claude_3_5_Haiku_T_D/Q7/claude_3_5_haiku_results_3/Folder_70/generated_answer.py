def all_even_ints_inclusive(nums):
    if len(nums) <= 32:
        return []
    subset = nums[28:33]
    return [num for num in subset if num % 2 == 0]