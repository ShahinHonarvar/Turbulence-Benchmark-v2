def all_pos_ints_inclusive(nums):
    """
            Returns a list of all positive integers from index 0 to index 4, both inclusive.

            Args:
                nums: A list of integers.

            Returns:
                A list of positive integers from index 0 to index 4, both inclusive. If no positive integers exist in the specified range, returns an empty list.
            """
    pos_ints = []
    for num in nums:
        if num >= 0:
            pos_ints.append(num)
    if not pos_ints:
        pos_ints = []
    return pos_ints[:5]