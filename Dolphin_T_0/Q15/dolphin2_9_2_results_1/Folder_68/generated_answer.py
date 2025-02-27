def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if i <= 8 and num % 2 != 0))