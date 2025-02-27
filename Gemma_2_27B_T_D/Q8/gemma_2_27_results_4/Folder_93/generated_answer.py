def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 19 and i < 94 and (num % 2 == 0)]