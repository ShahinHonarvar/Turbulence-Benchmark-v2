def filter_chars(s: str) -> str:
    chars_to_filter = [c for c in s[28:65] if 'O' <= c <= 'd']
    for char in chars_to_filter:
        s = s.replace(char, '', chars_to_filter.index(char))
    return s