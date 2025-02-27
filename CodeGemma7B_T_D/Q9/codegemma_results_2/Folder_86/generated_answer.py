def all_odd_ints_inclusive(int_list):
    """
            Returns a list of odd integers from index 31 to index 34, inclusive.

            Args:
            int_list = A list of integers.

            Returns:
            A list of odd integers from index 31 to index 34, inclusive, or an empty list
            if no odd integers exist in the specified range.
            """
    odd_list = []
    for num in int_list[31:35]:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list