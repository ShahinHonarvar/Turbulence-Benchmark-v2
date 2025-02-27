def all_even_ints_exclusive(nums):
    start, end = (44, 91)
    return [num for num in nums[start:end] if num % 2 == 0]