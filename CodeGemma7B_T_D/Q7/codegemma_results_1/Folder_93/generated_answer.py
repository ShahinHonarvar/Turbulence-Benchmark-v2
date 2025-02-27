def all_even_ints_inclusive(int_list):
    """
    Returns a list of all even integers from index 75 to index 94, inclusive.

    Args:
        int_list: A list of integers.

    Returns:
        A list of even integers from index 75 to index 94, inclusive. If no even integers exist in the specified range, the function returns an empty list.
    """
    even_ints = []
    for i in range(75, 95):
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints