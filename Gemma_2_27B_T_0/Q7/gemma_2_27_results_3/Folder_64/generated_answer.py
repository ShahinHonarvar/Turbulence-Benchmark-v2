def all_even_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i <= 4 and num % 2 == 0]