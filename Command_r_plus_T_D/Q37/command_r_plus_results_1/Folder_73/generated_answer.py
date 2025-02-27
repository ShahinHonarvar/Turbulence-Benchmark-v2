def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (22 <= i <= 85 and '7' <= c <= 'e')))
    return filtered_string