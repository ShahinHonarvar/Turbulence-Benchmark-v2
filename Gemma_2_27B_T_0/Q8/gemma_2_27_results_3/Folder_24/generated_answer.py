def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 13 and i < 66 and (num % 2 == 0)]