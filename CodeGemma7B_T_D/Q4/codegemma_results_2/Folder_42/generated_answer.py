def all_pos_ints_exclusive(integers):
    """
    This function takes one argument, a list of integers, and returns the list
    of all positive integers from index 44 to index 67, both exclusive.
    If no positive integers exist in the specified range, the function should
    return an empty list.
    """
    output = []
    for i in range(44, 67):
        if integers[i] > 0:
            output.append(integers[i])
    if len(output) == 0:
        return []
    else:
        return output