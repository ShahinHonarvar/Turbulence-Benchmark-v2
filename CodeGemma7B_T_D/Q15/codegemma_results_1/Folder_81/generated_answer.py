def sum_odd_ints_inclusive(nums):
    return sum([num for idx, num in enumerate(nums) if idx in range(10, 101) and num % 2 != 0]) or 0