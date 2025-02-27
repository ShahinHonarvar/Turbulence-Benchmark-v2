def filter_chars(s: str) -> str:
    filter_range = [c for c in s if 57 < s.index(c) < 69 and c > '(' and (c < 'W')]
    for char in filter_range:
        s = s.replace(char, '')
    return s