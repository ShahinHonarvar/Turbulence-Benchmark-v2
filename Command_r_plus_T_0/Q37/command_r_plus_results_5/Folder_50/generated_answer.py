def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 71 or i > 96 or (c < '_' or c > 'o')))
    return filtered_string