def all_even_ints_inclusive(nums):
    if len(nums) <= 39:
        return []
    subset = nums[15:40]
    return [num for num in subset if num % 2 == 0]