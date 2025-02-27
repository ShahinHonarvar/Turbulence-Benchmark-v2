def all_pos_ints_exclusive(nums):
    """
            Returns the list of all positive integers from index 59 to index 93, both exclusive.
            If no positive integers exist in the specified range, the function should return an empty list.
            """
    pos_ints = []
    for num in nums:
        if 59 < num < 93 and num > 0:
            pos_ints.append(num)
    return pos_ints if pos_ints else []