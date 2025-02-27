def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (19 <= i <= 90 and 'F' <= c <= 'h')))
    return filtered_string