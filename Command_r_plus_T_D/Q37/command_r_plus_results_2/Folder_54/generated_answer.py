def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (46 <= i <= 85 and '-' <= c <= 'X')))
    return filtered_string