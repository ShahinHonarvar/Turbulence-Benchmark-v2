def filter_chars(s: str) -> str:
    filtered_string = ''.join((ch for idx, ch in enumerate(s) if idx < 259 or idx > 502 or (ch < ',' or ch > '3')))
    return filtered_string