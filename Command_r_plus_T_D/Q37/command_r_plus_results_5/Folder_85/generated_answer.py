def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (28 <= i <= 65 and 'O' <= c <= 'd')))
    return filtered_string