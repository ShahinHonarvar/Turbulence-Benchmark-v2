def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 20 and i < 51 and (num % 2 != 0)]