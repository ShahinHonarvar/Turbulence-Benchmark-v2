def filter_chars(s: str) -> str:
    chars_to_remove = [c for c in s[71:95] if 'K' <= c <= 'a']
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s