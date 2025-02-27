def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 100 and i < 101 and (num % 2 != 0)]