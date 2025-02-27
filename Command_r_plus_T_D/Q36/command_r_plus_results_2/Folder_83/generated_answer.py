def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if (i < 72 or i > 93) or (c > '<' and c < 'J')))
    return filtered_string