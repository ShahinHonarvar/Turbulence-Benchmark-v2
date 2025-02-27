def all_ints_div_by_both_two_nums(nums):
    """
            Write a function called 'all_ints_div_by_both_two_nums' that takes one argument, a list of integers,
            and returns the list of all integers divisible by both 71 and 81 from index 14 to index 93, both inclusive.
            If no such integers exist in the specified range, the function should return an empty list.
            """
    result = []
    for i in nums[14:94]:
        if i % 71 == 0 and i % 81 == 0:
            result.append(i)
    return result