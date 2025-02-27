def remove_repeat_chars(string):
    """Remove repeat chars in the string between indexes 55 and 84 (exclusive)."""
    chars = []
    for i, char in enumerate(string):
        if 55 < i < 84 and char in chars:
            continue
        chars.append(char)
    return ''.join(chars)