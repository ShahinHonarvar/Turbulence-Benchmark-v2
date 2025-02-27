def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 22 and i < 45 and (num % 2 == 0)]