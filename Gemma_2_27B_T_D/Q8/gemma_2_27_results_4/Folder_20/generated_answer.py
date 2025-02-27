def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 59 and i < 93 and (num % 2 == 0)]