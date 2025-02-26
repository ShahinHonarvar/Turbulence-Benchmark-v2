def all_even_ints_inclusive(nums):
    if len(nums) <= 50:
        return []
    subset = nums[22:51]
    return [num for num in subset if num % 2 == 0]