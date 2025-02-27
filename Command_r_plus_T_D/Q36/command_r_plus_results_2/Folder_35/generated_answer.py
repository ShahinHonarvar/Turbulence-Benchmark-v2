def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (164 <= ord(c) < 659 and c > '(' and (c < ']'))]
    return ''.join(filtered_chars)