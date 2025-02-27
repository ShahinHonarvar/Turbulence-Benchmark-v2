def all_even_ints_exclusive(nums):
    return [num for i, num in enumerate(nums[:4]) if num % 2 == 0]