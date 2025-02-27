def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (71 <= i <= 94 and 'K' <= c <= 'a')))
    return filtered_string