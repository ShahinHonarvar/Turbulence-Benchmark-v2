def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (19 <= i <= 92 and '8' <= c <= 'm')))
    return filtered_string