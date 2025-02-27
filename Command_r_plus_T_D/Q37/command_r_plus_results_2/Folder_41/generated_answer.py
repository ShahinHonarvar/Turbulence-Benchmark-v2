def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not (26 <= ord(c) <= 64 and 'V' <= c <= 'o')))
    return filtered_string