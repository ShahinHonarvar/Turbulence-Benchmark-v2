def all_even_ints_inclusive(nums):
    if len(nums) <= 57:
        return []
    sublist = nums[56:58]
    return [num for num in sublist if num % 2 == 0]