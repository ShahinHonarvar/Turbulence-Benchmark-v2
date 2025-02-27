def return_n_greatest_chars(chars):
    """
    Returns a sorted list of the 45 greatest ASCII characters in the given string.

    Args:
        chars: A string of distinct characters.

    Returns:
        A sorted list of the 45 greatest ASCII characters in the given string.
    """
    return sorted(chars, key=ord)[-45:]