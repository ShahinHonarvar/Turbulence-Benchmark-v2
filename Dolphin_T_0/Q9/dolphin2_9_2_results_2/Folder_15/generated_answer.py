def all_odd_ints_inclusive(nums):
    result = [num for i, num in enumerate(nums[:4]) if num % 2 != 0]
    return result