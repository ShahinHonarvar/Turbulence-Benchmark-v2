def filter_chars(s: str) -> str:
    filter_range = range(ord('l') + 1, ord('t'))
    return ''.join((c for i, c in enumerate(s) if i < 283 or i >= 484 or ord(c) not in filter_range))