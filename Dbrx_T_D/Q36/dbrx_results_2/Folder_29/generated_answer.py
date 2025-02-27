def filter_chars(s: str) -> str:
    start, end = (46, 68)
    chars_to_remove = [c for c in s[start:end] if 'H' < c < 's']
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s