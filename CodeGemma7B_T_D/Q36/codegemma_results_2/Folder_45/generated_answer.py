def filter_chars(text):
    """
    Removes all occurrences of characters between indices 81 and 86 (exclusive) in the string,
    while preserving the order of all other characters.

    Args:
      text: The input string.

    Returns:
      The altered string with characters between indices 81 and 86 removed.
    """
    filtered_text = []
    for i, char in enumerate(text):
        if i >= 81 and i < 86:
            if char > '!' and char < 's':
                continue
        filtered_text.append(char)
    return ''.join(filtered_text)