def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if i >= 209 and i <= 556 and (num % 2 == 0)))