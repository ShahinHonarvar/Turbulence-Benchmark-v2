def all_ints_not_div_by_num(nums):
    """
    This function takes one argument, a list of integers, and returns the list of all integers not divisible by 16 from index 14 to index 48, both exclusive. If no such integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for num in nums[14:48]:
        if num % 16 != 0:
            result.append(num)
    return result