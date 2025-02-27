def sum_ints_div_by_either_nums(nums):
    """
    This function takes one argument, a list of integers, and returns the sum of all integers divisible by either 6 or 1 from index 3 to index 9, both inclusive. If no such integers exist in the specified range, the function should return 0.
    """
    sum = 0
    for num in nums[3:10]:
        if num % 6 == 0 or num % 1 == 0:
            sum += num
    return sum