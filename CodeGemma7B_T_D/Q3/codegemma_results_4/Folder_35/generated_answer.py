def all_pos_ints_inclusive(lst):
    """ Returns a list of all positive 
    integers from index 30 to index 48, both inclusive. 
    If no positive integers exist in the specified range, 
    the function should return an empty list.
    """
    res = []
    for i in range(30, 49):
        if lst[i] > 0:
            res.append(lst[i])
    return res