def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if i >= 26 and i <= 52 and (num % 2 == 0)))