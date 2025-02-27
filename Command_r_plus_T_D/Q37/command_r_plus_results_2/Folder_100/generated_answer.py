def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[88:91] if 'J' <= c <= 'Q']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s