def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 114 or i > 639 or (c < '!' or c > 'x')))
    return filtered_string