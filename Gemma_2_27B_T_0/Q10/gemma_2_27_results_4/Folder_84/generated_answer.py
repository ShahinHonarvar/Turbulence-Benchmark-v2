def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 50 and i < 92 and (num % 2 != 0)]