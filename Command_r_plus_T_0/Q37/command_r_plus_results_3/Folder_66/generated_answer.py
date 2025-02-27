def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not (27 <= ord(c) <= 85 and 'c' <= c <= 'i')))
    return filtered_string