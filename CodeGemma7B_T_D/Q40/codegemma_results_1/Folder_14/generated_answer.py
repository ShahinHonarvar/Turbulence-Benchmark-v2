def return_n_smallest_chars(str_in):
    """ Returns a list of the 69 characters of the given string with the smallest ASCII values.
    The list is sorted in ascending order. """
    return sorted(str_in, key=ord)[:69]