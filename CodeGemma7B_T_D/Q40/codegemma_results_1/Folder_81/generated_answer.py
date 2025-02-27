def return_n_smallest_chars(string):
    """
            Returns a list of the n smallest characters in a string.
            """
    list_of_chars = sorted(list(string), key=ord)
    return list_of_chars[:64]