def sum_odd_ints_inclusive(listo):
    """
    This function sums all odd integers from index 75 to index 85, inclusive.
    If no odd integers exist in the specified range, the function returns 0.
    """
    total = 0
    for i in range(75, 86):
        if i % 2 != 0:
            total += listo[i]
    return total or 0