def sum_odd_ints_inclusive(nums):
    return sum((num for idx, num in enumerate(nums) if idx in range(29, 94) and num % 2))