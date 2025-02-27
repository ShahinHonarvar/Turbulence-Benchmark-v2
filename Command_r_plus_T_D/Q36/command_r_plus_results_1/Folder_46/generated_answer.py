def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (19 < s.index(c) < 69 and c > '<' and (c < 'C'))]
    return ''.join(filtered_chars)