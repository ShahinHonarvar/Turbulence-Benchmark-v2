def all_pos_ints_inclusive(li):
    """
    This function takes one argument, a list of integers, and returns the list of all positive integers from index 62 to index 63, both inclusive.
    If no positive integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for num in li[62:64]:
        if num > 0:
            result.append(num)
    return result