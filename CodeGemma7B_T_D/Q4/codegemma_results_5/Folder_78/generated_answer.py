def all_pos_ints_exclusive(nums):
    """
            Args:
                nums: A list of integers.

            Returns:
                A list of all positive integers from index 20 to index 35, both exclusive. Empty if no positive integers exist in the specified range.
            """
    return [num for num in nums if num > 0 and 20 < nums.index(num) < 35]