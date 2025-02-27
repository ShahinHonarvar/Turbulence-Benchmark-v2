def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums[:5]) if i <= 4 and num % 2 != 0]