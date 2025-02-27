def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[14:75] if '9' < c < 'K']
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s