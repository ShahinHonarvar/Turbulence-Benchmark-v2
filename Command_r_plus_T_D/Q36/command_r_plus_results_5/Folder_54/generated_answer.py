def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[18:38] if ')' < c < 'P']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s