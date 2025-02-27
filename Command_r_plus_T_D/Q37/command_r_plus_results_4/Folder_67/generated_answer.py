def filter_chars(s: str) -> str:
    filter_range = [char for char in s[19:23] if ']' <= char <= 't']
    for char in filter_range:
        s = s.replace(char, '')
    return s