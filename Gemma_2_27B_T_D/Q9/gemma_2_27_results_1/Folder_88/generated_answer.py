def all_odd_ints_inclusive(nums):
    return [num for idx, num in enumerate(nums) if idx >= 4 and idx <= 8 and (num % 2 != 0)]