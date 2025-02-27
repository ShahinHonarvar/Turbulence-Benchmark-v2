def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (71 <= i <= 96 and '_' <= c <= 'o')))
    return filtered_string