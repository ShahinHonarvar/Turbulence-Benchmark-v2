def all_even_ints_inclusive(nums):
    return [num for idx, num in enumerate(nums) if idx >= 20 and idx <= 200 and (num % 2 == 0)]