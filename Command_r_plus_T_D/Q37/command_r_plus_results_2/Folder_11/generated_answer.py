def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 29 or i > 97 or c < '-' or (c > 'n')))
    return filtered_string