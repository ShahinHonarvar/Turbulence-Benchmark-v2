def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not ('V' <= c <= 'o' and 26 <= ord(c) <= 64)))
    return filtered_string