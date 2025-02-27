def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 11 or i > 32 or (c < '!' or c > '@')))
    return filtered_string