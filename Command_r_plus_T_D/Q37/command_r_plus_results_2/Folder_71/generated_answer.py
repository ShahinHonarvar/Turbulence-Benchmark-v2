def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not (32 <= ord(c) <= 46 and '0' <= c <= 'k')))
    return filtered_string