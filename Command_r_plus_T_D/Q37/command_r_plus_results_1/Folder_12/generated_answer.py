def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if (i < 19 or i > 90) or (c < 'F' or c > 'h')))
    return filtered_string