def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums[:6]) if i <= 5 and num % 2 != 0]