def sum_ints_div_by_either_nums(nums):
    """
    Returns the sum of all integers divisible by either -30 or -88 from index 57 to index 84, both inclusive. If no such integers exist in the specified range, the function should return 0.
    """
    return sum((n for n in nums[57:85] if n % -30 == 0 or n % -88 == 0)) or 0