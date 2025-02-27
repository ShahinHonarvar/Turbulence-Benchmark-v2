def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 17 and i < 60 and (num % 2 != 0)]