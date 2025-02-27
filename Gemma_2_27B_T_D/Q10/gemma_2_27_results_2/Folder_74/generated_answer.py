def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 13 and i < 70 and (num % 2 != 0)]