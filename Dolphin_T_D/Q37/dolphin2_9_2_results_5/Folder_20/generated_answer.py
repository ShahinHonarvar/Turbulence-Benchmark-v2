def filter_chars(string: str) -> str:
    return ''.join([c for c in string if 26 <= string.index(c) <= 96 and 'm' <= c <= 'w'])