def all_even_ints_exclusive(nums):
    return [num for idx, num in enumerate(nums) if idx > 12 and idx < 66 and (num % 2 == 0)]