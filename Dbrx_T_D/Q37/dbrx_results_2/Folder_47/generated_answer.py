def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[38:55] if '8' <= c <= 'r']
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s