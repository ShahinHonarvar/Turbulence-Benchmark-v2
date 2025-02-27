def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 41 or i > 64 or (c < 'K' or c > ']')))
    return filtered_string