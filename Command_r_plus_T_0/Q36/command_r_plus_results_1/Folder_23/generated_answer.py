def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[21:25] if '5' < c < '}']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s