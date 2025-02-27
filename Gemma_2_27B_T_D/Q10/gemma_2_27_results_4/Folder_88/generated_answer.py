def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 1 and i < 8 and (num % 2 != 0)]