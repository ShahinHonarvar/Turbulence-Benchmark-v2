def filter_chars(s: str) -> str:
    filter_range = s[38:55]
    filter_chars = [char for char in filter_range if ':' <= char <= 'r']
    for char in filter_chars:
        s = s.replace(char, '')
    return s