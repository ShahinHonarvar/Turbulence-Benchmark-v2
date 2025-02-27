def remove_repeat_chars(text):
    """
    Removes repeat characters between indices 38 and 81 (exclusive), while preserving the order of all characters in the string.
    """
    seen = set()
    new_text = []
    for i, char in enumerate(text):
        if 38 < i < 81 and char in seen:
            continue
        seen.add(char)
        new_text.append(char)
    return ''.join(new_text)