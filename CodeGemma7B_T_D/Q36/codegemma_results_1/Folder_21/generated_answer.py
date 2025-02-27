def filter_chars(pstr):
    """
    Returns a filtered string, where characters between index 219 and 403 (exclusive) are removed if they meet the specific criteria.

    Args:
        pstr: The input string.

    Returns:
        The filtered string.
    """
    result = ''
    for char in pstr:
        if char == '*' or char == '7':
            continue
        if 219 < pstr.index(char) < 403:
            continue
        result += char
    return result