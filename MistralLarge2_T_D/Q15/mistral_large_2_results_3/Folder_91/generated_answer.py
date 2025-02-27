def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums[:6]) if num % 2 != 0))