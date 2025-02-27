def all_ints_not_div_by_num(nums):
    """
            This function returns the list of all integers not divisible by a number from the specified range.

            Args:
                nums: A list of integers.

            Returns:
                A list of all integers not divisible by the number from the specified range. If no such integers exist, the function returns an empty list.
            """
    result = []
    for i in range(43, 77):
        if nums[i] % 84 != 0:
            result.append(nums[i])
    return result