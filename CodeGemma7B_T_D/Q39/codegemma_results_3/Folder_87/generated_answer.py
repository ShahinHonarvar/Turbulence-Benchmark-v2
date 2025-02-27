def return_n_greatest_chars(chars: str) -> list[str]:
    """
    Function to return the n greatest characters from a string of distinct characters.

    Args:
    chars: A string of distinct characters.

    Returns:
    A sorted list of n greatest characters of the given string.
    """
    chars_sorted = sorted(chars)
    return chars_sorted[:24]