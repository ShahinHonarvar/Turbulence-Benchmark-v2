def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (41 <= i <= 79 and 'f' <= c <= '|')))
    return filtered_string