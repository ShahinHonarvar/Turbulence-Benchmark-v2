def sum_odd_ints_inclusive(nums):
    return sum((n for i, n in enumerate(nums) if 22 <= i <= 88 and n % 2 != 0))