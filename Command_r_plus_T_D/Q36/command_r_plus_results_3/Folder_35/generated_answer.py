def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (163 < s.index(c) < 658 and c > '(' and (c < ']'))]
    return ''.join(filtered_chars)