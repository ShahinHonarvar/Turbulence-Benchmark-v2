def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 28 or i > 65 or (c < 'O' or c > 'd')))
    return filtered_string