def insert_before_character(s):
    """
    Inserts character 'N' immediately preceding any occurrences of character 'B'.

    Args:
        s: The string to modify.

    Returns:
        The modified string.
    """
    result = ''
    for char in s:
        if char == 'B':
            result += 'N' + char
        else:
            result += char
    return result