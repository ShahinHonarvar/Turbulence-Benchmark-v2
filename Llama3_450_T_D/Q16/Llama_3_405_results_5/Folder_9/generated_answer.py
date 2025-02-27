def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if 70 <= i <= 200 and num % 2 == 0))