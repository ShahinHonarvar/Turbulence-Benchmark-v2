def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not (46 <= ord(c) <= 85 and '-' <= c <= 'X')))
    return filtered_string