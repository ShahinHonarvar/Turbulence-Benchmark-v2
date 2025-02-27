def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[69:97] if 'V' < c < 'j']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s