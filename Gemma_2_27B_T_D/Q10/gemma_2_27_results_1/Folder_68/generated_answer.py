def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i < 8 and i > 0 and (num % 2 != 0)]