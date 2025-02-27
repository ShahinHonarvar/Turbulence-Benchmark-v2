def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if 31 <= i <= 72 and num % 2 != 0))