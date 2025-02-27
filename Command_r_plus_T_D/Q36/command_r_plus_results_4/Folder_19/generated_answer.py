def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (77 <= s.index(c) < 87 and c > ';' and (c < 'r'))]
    return ''.join(filtered_chars)