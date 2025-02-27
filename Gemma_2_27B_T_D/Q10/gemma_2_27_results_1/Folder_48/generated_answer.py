def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 385 and i < 999 and (num % 2 != 0)]