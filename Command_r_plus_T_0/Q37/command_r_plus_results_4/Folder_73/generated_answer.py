def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 22 or i > 85 or (c < '7' or c > 'e')))
    return filtered_string