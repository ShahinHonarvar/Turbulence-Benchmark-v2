def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not 32 <= ord(c) <= 72 or (c > 'M' and c < 'j')))
    return filtered_string