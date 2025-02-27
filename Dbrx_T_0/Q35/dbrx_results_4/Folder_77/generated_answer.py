def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[355:988])
    for char in chars_to_remove:
        if s[355:988].count(char) > 1:
            s = s.replace(char, '', s[355:988].index(char))
    return s