def composite_nums_between_indices(int_list):
    """
    Args:
        int_list: A list of positive integers

    Returns:
        A set of all composite numbers in the given list that are between index 28 to index 38, both inclusive. If no composite number exists in the specified range, the function should return an empty set.
    """
    composites = set()
    for i in range(28, 39):
        if int_list[i] % 2 == 0 or int_list[i] % 3 == 0:
            composites.add(int_list[i])
    return composites