def return_n_smallest_chars(characters):
    """
            Returns a list of the two characters with the smallest ASCII values in a given string.
            """
    char_list = list(characters)
    char_list.sort()
    return char_list[:2]