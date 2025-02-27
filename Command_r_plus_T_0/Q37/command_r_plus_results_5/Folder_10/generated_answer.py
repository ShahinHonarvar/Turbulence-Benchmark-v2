def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 63 or i > 84 or (c < 'E' or c > '~')))
    return filtered_string