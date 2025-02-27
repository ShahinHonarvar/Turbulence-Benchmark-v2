def sum_odd_ints_inclusive(nums):
    return sum([num for i, num in enumerate(nums) if i >= 29 and i <= 51 and (num % 2 != 0)])