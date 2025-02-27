def filter_chars(s: str) -> str:
    start, end = (32, 84)
    filter_range = range(ord('m') + 1, ord('w'))
    return ''.join((c for i, c in enumerate(s) if i < start or i > end or ord(c) not in filter_range))