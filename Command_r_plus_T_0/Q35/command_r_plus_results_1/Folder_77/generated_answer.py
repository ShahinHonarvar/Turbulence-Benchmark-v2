def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[355:988])
    for char in repeat_chars:
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s