def filter_chars(s: str) -> str:
    filter_range = [c for c in s if 323 < s.index(c) < 526 and c > ')' and (c < 'O')]
    for char in filter_range:
        s = s.replace(char, '')
    return s