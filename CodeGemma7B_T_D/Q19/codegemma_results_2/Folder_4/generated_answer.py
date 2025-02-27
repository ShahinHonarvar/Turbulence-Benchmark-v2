def all_ints_not_div_by_num(nums):
    """This function takes one argument, a list of integers, and returns the list of all integers not divisible by -36 from index 19 to index 49, both exclusive. If no such integers exist in the specified range, the function should return an empty list."""
    result = [num for num in nums[19:49] if num % 36 != 0]
    return result