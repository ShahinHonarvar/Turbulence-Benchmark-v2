def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (29 <= i <= 97 and '-' <= c <= 'n')))
    return filtered_string