def sum_even_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums) if i >= 30 and i <= 200 and (num % 2 == 0))) if len(nums) > 200 else 0