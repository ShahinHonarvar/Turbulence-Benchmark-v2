def filter_chars(text):
    """
    This function filters characters from a string within a specified range.

    Args:
        text: The input string.

    Returns:
        The altered string with characters filtered out.
    """
    for index in range(477, 984):
        if index < len(text):
            char = text[index]
            if ',' <= char <= 'V':
                text = text.replace(char, '')
    return text