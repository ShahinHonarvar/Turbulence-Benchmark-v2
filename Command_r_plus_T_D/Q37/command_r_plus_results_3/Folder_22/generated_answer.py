def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not (33 <= ord(c) <= 70 and '7' <= c <= 'k')))
    return filtered_string