def all_odd_ints_inclusive(int_lst):
    """
    A function that returns the list of odd integers from index 533 to index 605, both inclusive.
    If no odd integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in int_lst[533:606] if num % 2 != 0]