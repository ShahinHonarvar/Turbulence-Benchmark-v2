def all_odd_ints_exclusive(nums):
    """List comprehension to return all odd numbers in the range from 60 to 200 (exclusive)"""
    return [num for num in nums if num % 2 != 0 and 60 < num < 200]