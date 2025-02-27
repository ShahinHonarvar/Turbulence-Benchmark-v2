def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums[:10]) if num % 2 != 0]