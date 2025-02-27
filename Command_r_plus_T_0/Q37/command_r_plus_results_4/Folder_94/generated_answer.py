def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (51 <= i <= 96 and 'X' <= c <= 'p')))
    return filtered_string