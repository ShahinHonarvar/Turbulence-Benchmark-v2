def all_even_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if num % 2 == 0 and 0 <= i <= 10]