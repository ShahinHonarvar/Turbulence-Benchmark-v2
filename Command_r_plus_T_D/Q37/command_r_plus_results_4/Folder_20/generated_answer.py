def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not (25 <= ord(c) <= 97 and 'm' <= c <= 'w')))
    return filtered_string