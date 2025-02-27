def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 12 or i > 88 or (c < '&' or c > 'v')))
    return filtered_string