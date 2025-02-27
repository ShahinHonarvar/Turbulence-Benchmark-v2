def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if i >= 31 and i <= 72 and (num % 2 == 0)))