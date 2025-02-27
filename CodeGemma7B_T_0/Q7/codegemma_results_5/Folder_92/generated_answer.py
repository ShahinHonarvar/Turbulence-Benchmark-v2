def all_even_ints_inclusive(nums):
    return [num for num in nums if num % 2 == 0 and num >= 0 and (num <= 1)]