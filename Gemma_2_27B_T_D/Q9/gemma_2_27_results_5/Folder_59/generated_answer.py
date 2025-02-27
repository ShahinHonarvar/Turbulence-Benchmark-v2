def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i <= 9 and i >= 0 and (num % 2 != 0)]