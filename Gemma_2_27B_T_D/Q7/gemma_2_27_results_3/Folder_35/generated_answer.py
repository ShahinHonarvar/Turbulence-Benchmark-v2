def all_even_ints_inclusive(nums):
    return [num for idx, num in enumerate(nums) if idx >= 30 and idx <= 48 and (num % 2 == 0)]