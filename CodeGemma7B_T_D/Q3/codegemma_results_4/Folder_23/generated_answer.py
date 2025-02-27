def all_pos_ints_inclusive(nums):
    """
            Returns the list of all positive integers from index 52 to index 71, both inclusive.

            Args:
                nums: A list of integers.

            Returns:
                A list of positive integers in the specified range, or an empty list if no positive integers exist.
            """
    pos_ints = []
    for i in range(52, 72):
        if i < len(nums) and nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints