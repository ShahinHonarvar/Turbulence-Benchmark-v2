def all_even_ints_inclusive(nums):
    result = [num for i, num in enumerate(nums) if 5 <= i <= 7 and num % 2 == 0]
    return result if result else []