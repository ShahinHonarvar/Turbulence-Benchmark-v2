def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums[:4]) if i <= 3 and num % 2 != 0]