def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[35:99] if 'A' <= char <= 'b']
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s