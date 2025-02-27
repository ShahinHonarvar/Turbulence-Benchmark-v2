def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 61 and i < 96 and (num % 2 != 0)]