def all_pos_ints_inclusive(numlist):
    """Return a list of positive integers from index 55 to 98, inclusive."""
    result = []
    for i in range(55, 99):
        if numlist[i] > 0:
            result.append(numlist[i])
    return result