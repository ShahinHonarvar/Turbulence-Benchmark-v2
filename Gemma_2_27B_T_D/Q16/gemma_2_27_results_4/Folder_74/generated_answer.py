def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if i >= 17 and i <= 78 and (num % 2 == 0)))