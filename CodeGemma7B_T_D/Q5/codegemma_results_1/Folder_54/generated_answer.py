def all_neg_ints_inclusive(lst):
    """
    This function takes one argument, a list of integers, and returns the list of all negative integers from index 34 to index 55, both inclusive. If no negative integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for i in range(34, 56):
        if lst[i] < 0:
            result.append(lst[i])
    return result