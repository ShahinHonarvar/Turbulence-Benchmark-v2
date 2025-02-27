def filter_chars(s: str) -> str:
    filter_func = lambda c: '!' <= c <= 's'
    start, end = (81, 86)
    return ''.join(filter(lambda c: not filter_func(c), s[:start])) + s[start:end] + ''.join(filter(lambda c: not filter_func(c), s[end:]))