def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums[:2], start=0) if num % 2 != 0]