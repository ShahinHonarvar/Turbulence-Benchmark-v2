def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums[19:93]) if i >= 19 and i <= 92 and (num % 2 == 0)))