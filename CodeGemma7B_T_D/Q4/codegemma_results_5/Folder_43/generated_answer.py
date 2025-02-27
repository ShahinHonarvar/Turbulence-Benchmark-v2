def all_pos_ints_exclusive(nums):
    """
            Returns a list of all positive integers from index 38 to index 77, both exclusive.

            Args:
                nums: A list of integers.

            Returns:
                A list of positive integers from index 38 to index 77, both exclusive. If no positive integers exist in the specified range, an empty list is returned.
            """
    pos_ints = []
    for num in nums:
        if num > 0 and 38 < nums.index(num) < 77:
            pos_ints.append(num)
    return pos_ints