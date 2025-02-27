def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[31:39] if ord(';') <= ord(c) <= ord('g')]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s