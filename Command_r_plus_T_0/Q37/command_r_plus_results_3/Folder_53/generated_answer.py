def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (83 <= i <= 99 and '*' <= c <= 'j')))
    return filtered_string