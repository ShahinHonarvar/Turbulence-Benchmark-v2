def return_n_smallest_chars(string):
    """
            Returns a list of 32 characters from the given string with the smallest ASCII values.
            """
    sorted_chars = sorted(string)
    return sorted_chars[:32]