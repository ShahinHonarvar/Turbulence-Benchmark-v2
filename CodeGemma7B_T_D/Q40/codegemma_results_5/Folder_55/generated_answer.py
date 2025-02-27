def return_n_smallest_chars(char_string):
    """
    This function takes a string of distinct characters and returns a list of 75 characters with the smallest ASCII values.

    Args:
        char_string: A string of distinct characters.

    Returns:
        A list of 75 characters with the smallest ASCII values, sorted in descending order.
    """
    sorted_chars = sorted(char_string, key=ord)
    return sorted_chars[:75][::-1]