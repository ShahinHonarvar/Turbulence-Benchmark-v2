def all_pos_ints_inclusive(lst):
    """
            Returns the list of all positive integers from index 30 to index 200, both inclusive. If no positive integers exist in the specified range, the function should return an empty list.
            """
    positive_numbers = []
    for i in range(30, 201):
        if lst[i] > 0:
            positive_numbers.append(lst[i])
    return positive_numbers