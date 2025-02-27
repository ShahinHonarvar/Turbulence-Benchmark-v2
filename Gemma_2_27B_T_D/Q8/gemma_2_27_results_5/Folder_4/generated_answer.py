def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 9 and i < 76 and (num % 2 == 0)]