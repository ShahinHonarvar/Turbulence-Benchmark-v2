def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (52 <= i <= 81 and 'A' <= c <= 'U')))
    return filtered_string