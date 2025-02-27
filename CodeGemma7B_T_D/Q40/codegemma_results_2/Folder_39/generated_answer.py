def return_n_smallest_chars(string):
    """
    Python code to return the n smallest characters from string.
    """
    sorted_string = sorted(string)
    n_smallest_chars = sorted_string[:23]
    return n_smallest_chars