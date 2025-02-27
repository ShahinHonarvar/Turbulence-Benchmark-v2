def filter_chars(s: str) -> str:
    filter_chars = [c for c in s[27:85] if 'c' <= c <= 'i']
    for char in filter_chars:
        s = s.replace(char, '', 1)
    return s