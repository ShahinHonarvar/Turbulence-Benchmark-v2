def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 25 and i <= 59 and (num % 2 != 0)]