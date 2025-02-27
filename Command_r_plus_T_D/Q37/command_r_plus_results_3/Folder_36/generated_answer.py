def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 259 or i > 502 or (c < ',' or c > '3')))
    return filtered_string