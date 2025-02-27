def all_pos_ints_exclusive(nums):
    """
            Returns a list of all positive integers from index 111 to index 473, both exclusive.

            Args:
                nums: A list of integers.

            Returns:
                A list of positive integers from index 111 to index 473, both exclusive. If no positive integers exist in the specified range, returns an empty list.
            """
    pos_ints = []
    for i in range(111, 473):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints