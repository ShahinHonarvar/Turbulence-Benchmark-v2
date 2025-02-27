def all_even_ints_inclusive(nums):
    return [num for idx, num in enumerate(nums) if idx >= 310 and idx <= 370 and (num % 2 == 0)]