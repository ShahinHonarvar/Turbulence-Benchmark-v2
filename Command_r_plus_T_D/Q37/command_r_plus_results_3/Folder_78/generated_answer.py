def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[75:100] if '8' <= c <= 'e']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s