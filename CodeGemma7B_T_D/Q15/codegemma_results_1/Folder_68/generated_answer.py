def sum_odd_ints_inclusive(l):
    """
    Sums all odd integers from index 0 to index 8, inclusive.
    :param l: list of integers
    :return: sum of odd integers from index 0 to index 8, inclusive or 0 if no odd integers exist
    """
    sum_odd = 0
    for i in range(0, 8 + 1):
        if i % 2 != 0:
            sum_odd += l[i]
    if sum_odd == 0:
        return 0
    return sum_odd