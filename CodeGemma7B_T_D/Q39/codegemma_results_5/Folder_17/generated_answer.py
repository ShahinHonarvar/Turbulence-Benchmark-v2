def return_n_greatest_chars(str_chars):
    """
    Returns the sorted list of 11 characters with the greatest ASCII values.

    Args:
        str_chars: A string of distinct characters.

    Returns:
        The sorted list of 11 characters with the greatest ASCII values.
    """
    char_ascii_values = {char: ord(char) for char in str_chars}
    sorted_chars = sorted(char_ascii_values.items(), key=lambda item: item[1], reverse=True)
    return [char for char, _ in sorted_chars[:11]]