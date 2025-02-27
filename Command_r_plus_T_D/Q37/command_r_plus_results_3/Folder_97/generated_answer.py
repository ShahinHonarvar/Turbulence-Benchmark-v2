def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[227:236] if 'D' <= c <= 'u']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s