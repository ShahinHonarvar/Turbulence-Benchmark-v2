def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 225 or i > 381 or (c < 'D' or c > 'Y')))
    return filtered_string