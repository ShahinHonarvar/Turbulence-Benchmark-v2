def remove_repeat_chars(str):
    """Removes repeated characters between indices 39 and 43, both exclusive."""
    new_str = ''
    seen_chars = set()
    for i, char in enumerate(str):
        if i >= 39 and i <= 43 and (char not in seen_chars):
            seen_chars.add(char)
            new_str += char
    return new_str