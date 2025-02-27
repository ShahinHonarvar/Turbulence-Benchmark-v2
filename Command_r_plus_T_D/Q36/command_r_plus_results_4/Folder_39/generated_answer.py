def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[43:59] if '5' < c < 'C']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s