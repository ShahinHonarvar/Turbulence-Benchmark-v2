def filter_chars(str):
    """
    Filters out characters between indices 29 and 33 (exclusive) in a given string.

    Args:
        str: The string to filter.

    Returns:
        The altered string with filtered characters.
    """
    filtered_str = ''
    for i, char in enumerate(str):
        if i < 29 or i >= 33 or char <= '%' or (char >= 'a'):
            filtered_str += char
    return filtered_str