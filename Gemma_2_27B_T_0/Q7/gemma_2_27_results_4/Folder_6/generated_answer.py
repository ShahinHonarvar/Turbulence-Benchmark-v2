def all_even_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 10 and i <= 66 and (num % 2 == 0)]