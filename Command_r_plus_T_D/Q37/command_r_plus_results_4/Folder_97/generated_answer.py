def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if i < 227 or i > 235 or (c < 'D' or c > 'u')))
    return filtered_string