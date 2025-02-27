def all_even_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 19 and i <= 92 and (num % 2 == 0)]