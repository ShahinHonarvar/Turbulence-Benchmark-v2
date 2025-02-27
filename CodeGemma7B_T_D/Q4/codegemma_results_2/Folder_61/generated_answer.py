def all_pos_ints_exclusive(int_list):
    """
    Takes a list of integers and returns a list of all positive integers from
    index 0 to index 7, both exclusive. If no positive integers exist
    in the specified range, the function should return an empty list.

    >>> all_pos_ints_exclusive([2, -1, -3, 4, -5, 7, 6])
    [1, 2, 3, 4, 5, 6]

    >>> all_pos_ints_exclusive([0, 0, 0, -1, -2, -3, -4])
    []
    """
    res = []
    for i in range(1, 8):
        if i in int_list:
            res.append(i)
    return res