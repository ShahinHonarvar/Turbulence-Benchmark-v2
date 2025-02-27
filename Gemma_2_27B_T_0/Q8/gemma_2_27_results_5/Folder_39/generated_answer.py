def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 43 and i < 99 and (num % 2 == 0)]