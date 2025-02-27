def all_even_ints_inclusive(list_of_integers):
    """
    This function takes one argument, a list of integers, and returns the list of all even integers from index 56 to index 82, both inclusive. If no even integers exist in the specified range, the function should return an empty list.

    Args:
        list_of_integers: A list of integers.

    Returns:
        A list of even integers from index 56 to index 82, both inclusive. If no even integers exist in the specified range, an empty list is returned.
    """
    even_integers = []
    for i in range(56, 83):
        if list_of_integers[i] % 2 == 0:
            even_integers.append(list_of_integers[i])
    return even_integers