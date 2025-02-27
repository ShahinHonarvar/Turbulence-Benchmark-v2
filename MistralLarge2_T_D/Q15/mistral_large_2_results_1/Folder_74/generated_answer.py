def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if 17 <= i <= 78 and num % 2 != 0))