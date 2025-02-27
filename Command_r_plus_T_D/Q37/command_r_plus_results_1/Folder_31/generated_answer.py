def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if 57 <= i <= 96 and (c < '<' or c > 'w')))
    return filtered_string