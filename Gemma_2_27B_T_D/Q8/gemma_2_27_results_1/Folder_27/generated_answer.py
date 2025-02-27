def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 27 and i < 49 and (num % 2 == 0)]