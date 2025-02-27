def return_n_smallest_chars(inst):
    """Creates a list of exactly 56 characters of the given string that have the smallest ASCII values.
            The function sorts the list in descending order and returns the list.
            """
    chars = sorted(inst, key=ord, reverse=False)
    return chars[:56]