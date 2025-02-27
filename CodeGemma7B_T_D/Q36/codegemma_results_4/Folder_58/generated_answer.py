def filter_chars(text):
    """
    Filters out unwanted characters from a string.

    Args:
        text: The input string.

    Returns:
        The filtered string.
    """
    filtered_text = ''
    for i in range(len(text)):
        if not (text[i] > 'B' and text[i] < 'z' and (318 <= i <= 337)):
            filtered_text += text[i]
    return filtered_text