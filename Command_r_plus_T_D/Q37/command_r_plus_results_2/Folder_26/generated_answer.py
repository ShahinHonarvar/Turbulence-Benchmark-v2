def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 20 or i > 62 or (c < 'i' or c > 'k')))
    return filtered_string