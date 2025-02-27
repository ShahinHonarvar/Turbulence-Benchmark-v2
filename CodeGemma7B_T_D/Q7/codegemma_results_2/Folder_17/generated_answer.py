def all_even_ints_inclusive(list_of_integers):
    """Returns a list of all even integers from index 62 to index 78, 
    both inclusive. If no even integers exist in the specified range, 
    the function should return an empty list.
    """
    all_even = []
    for integer in list_of_integers[62:79]:
        if integer % 2 == 0:
            all_even.append(integer)
    return all_even