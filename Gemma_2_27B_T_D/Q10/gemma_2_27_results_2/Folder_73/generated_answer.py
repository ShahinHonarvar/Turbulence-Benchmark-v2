def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 36 and i < 85 and (num % 2 != 0)]