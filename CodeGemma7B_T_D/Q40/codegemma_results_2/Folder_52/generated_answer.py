def return_n_smallest_chars(string):
    """
            Takes one argument, a string of distinct characters and creates
            a list of exactly 68 characters of the given string that have the
            smallest ASCII values. The function should sort the list in ascending
            order and returns the list.
            """
    smallest_chars = sorted([char for char in string][:68])
    return smallest_chars