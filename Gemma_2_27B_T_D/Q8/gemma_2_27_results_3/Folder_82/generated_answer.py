def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if num % 2 == 0 and 20 < i < 200]