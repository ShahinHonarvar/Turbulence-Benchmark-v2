def return_n_smallest_chars(chars):
    """
            The function takes one argument, a string of distinct characters and creates a list of exactly 8 characters of the given string that have the smallest ASCII values.
            The function should sort the list in ascending order and returns the list.
            """
    char_list = list(chars)
    char_list.sort()
    return char_list[:8]