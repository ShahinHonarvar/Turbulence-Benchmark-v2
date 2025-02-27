def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 25 and i < 80 and (num % 2 == 0)]