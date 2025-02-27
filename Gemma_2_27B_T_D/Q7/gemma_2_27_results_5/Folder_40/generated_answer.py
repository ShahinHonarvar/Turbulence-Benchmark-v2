def all_even_ints_inclusive(nums):
    return [num for i, num in enumerate(nums[:3]) if i <= 2 and num % 2 == 0]