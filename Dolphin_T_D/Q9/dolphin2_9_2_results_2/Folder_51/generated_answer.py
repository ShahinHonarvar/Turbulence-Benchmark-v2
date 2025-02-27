def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums, start=1) if i <= 8 and num % 2 != 0]