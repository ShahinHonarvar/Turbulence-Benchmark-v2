def return_n_smallest_chars(text):
    """
    Returns a list of the n smallest characters in a string, sorted in descending order.

    Args:
        text: A string of distinct characters.

    Returns:
        A list of the n smallest characters in the string, sorted in descending order.
    """
    n = 79
    return sorted(text, key=ord, reverse=True)[:n]