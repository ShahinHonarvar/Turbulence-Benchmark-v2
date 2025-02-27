def all_ints_not_div_by_num(nums):
    """
            This function returns a list of all integers in a given list not divisible by -97 from index 32 to index 54, both exclusive.

            Args:
                nums: A list of integers.

            Returns:
                A list of integers, or an empty list if no integers in the specified range are not divisible by -97.
            """
    return [num for num in nums[32:54] if not num % -97]