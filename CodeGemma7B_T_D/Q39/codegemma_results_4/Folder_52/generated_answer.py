def return_n_greatest_chars(text, n):
    """
    Returns the n greatest characters from a string.

    Args:
        text: The string to return the greatest characters from.
        n: The number of greatest characters to return.

    Returns:
        A list of the n greatest characters from the string sorted in ascending order.
    """
    sorted_chars = sorted(text, key=ord, reverse=True)
    return sorted_chars[:n]