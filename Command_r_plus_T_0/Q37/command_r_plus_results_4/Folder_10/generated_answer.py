def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (63 <= i <= 84 and 'E' <= c <= '~')))
    return filtered_string