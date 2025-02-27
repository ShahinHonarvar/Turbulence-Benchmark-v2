def all_neg_ints_inclusive(int_list):
    """
    Returns a list of all negative integers from index 0 to index 6, both inclusive.
    """
    negative_ints = []
    for i in range(len(int_list)):
        if int_list[i] < 0 and i >= 0 and (i <= 6):
            negative_ints.append(int_list[i])
    return negative_ints