def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 12 or i > 77 or (c < ':' or c > 'L')))
    return filtered_string