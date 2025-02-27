def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (27 <= i <= 85 and '!' <= c <= 'B')))
    return filtered_string