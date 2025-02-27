def sum_odd_ints_inclusive(nums):
    return sum((num for index, num in enumerate(nums[:4]) if num % 2 != 0))