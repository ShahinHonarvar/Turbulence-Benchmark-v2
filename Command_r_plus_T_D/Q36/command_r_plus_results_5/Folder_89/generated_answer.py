def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[57:69] if c > '(' and c < 'W']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s