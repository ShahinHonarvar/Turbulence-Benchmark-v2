def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 12 and i <= 92 and (num % 2 != 0)]