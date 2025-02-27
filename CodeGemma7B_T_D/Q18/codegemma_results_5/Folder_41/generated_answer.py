def sum_ints_div_by_either_nums(nums):
    """
    Returns the sum of all integers divisible by either 6 or -3 between indices 0 and 9, inclusive.

    >>> sum_ints_div_by_either_nums([6, -3, 12, -9, 0, 15, -18, 21, 30, -36])
    66

    >>> sum_ints_div_by_either_nums([1, 2, 3, 4, 5])
    0
    """
    count = 0
    for i in range(10):
        if nums[i] % 6 == 0 or nums[i] % -3 == 0:
            count += nums[i]
    return count