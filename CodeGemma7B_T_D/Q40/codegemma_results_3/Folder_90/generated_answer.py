def return_n_smallest_chars(given_str):
    """
    Function to return the smallest n characters from a given string.

    Args:
        given_str: A string of distinct characters.

    Returns:
        A list of exactly 24 characters of the given string with the smallest ASCII values.
    """
    sorted_str = given_str[:]
    sorted_str.sort()
    smallest_chars = sorted_str[:24]
    smallest_chars.reverse()
    return smallest_chars