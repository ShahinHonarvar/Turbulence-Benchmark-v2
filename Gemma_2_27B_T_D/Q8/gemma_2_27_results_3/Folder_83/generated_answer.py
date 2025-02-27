def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 90 and i < 200 and (num % 2 == 0)]