def all_pos_ints_exclusive(nums):
    """
            This function takes a list of integers and returns the list of all positive integers from
            index 15 to index 40, both exclusive. If no positive integers exist
            in the specified range, the function should return an empty list.

            Args:
                nums: A list of integers.

            Returns:
                A list of positive integers from index 15 to index 40, both exclusive. If no
                positive integers exist in the specified range, the function should return an
                empty list.
            """
    positive_ints = []
    for num in nums:
        if num > 0 and num >= 15 and (num < 40):
            positive_ints.append(num)
    return positive_ints