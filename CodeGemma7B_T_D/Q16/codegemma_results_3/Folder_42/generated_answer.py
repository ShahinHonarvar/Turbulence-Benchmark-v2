def sum_even_ints_inclusive(nums):
    """
    sum of even from position 29 to 79 inclusive
    """
    return sum([num for num in nums[29:80] if num % 2 == 0]) or 0