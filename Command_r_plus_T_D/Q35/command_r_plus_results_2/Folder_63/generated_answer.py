def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[81:86])
    for char in chars_to_remove:
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s