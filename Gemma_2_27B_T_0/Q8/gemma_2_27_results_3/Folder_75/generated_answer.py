def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 20 and i < 36 and (num % 2 == 0)]