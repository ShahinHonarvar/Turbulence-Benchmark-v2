def filter_chars(text):
    """
    Filters characters in a string based on their position and value.

    Args:
    text: The input string.

    Returns:
    A string with filtered characters.
    """
    text_list = list(text)
    for i in range(331, 713):
        if text_list[i] > 'M' and text_list[i] < '_':
            text_list[i] = ''
    return ''.join(text_list)