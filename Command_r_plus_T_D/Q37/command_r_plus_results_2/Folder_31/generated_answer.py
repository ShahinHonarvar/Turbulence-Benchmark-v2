def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 57 or i > 96 or (c < '<' or c > 'w')))
    return filtered_string