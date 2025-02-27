def all_neg_ints_inclusive(lst):
    """
        Returns the list of all negative integers from index 310 to index 370, both inclusive.
        If no negative integers exist in the specified range, the function should return an empty list.
        """
    output = []
    for i in range(310, 371):
        if lst[i] < 0:
            output.append(lst[i])
    if not output:
        return []
    return output