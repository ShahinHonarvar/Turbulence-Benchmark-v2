def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if i >= 28 and i <= 40 and (num % 2 == 0)))