def sum_ints_div_by_either_nums(nums):
    """ sum_ints_div_by_either_nums takes one argument, a list of integers,
    and returns the sum of all integers divisible by either -24 or -11 from index 55 to index 84, both inclusive.
    If no such integers exist in the specified range, the function should return 0.
    """
    sum_of_nums = 0
    for num in nums[55:85]:
        if num % -24 == 0 or num % -11 == 0:
            sum_of_nums += num
    return sum_of_nums