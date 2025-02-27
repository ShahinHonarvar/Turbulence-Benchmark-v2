def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if not ('f' < c < '{' and 81 < i < 89)))