def filter_chars(s: str) -> str:
    filter_range = [char for char in s[0:2] if '*' <= char <= 's']
    return ''.join((char for char in s if char not in filter_range))