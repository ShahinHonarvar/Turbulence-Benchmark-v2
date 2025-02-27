def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 15 and i < 40 and (num % 2 != 0)]