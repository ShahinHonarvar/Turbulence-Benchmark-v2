def composite_nums_between_indices(some_list):
    """
    This function takes one argument, a list of positive integers.
    The function should return the set of all composite numbers in the given list that are
    between index 75 to index 94, both inclusive.
    If no composite number exists in the specified range, the function should return an
    empty set.
    """
    composites = set()
    for i in range(75, 95):
        if some_list[i] % 2 == 0 or some_list[i] % 3 == 0:
            composites.add(some_list[i])
    returncomposites