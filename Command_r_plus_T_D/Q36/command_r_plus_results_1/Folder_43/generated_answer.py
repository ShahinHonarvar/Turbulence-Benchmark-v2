def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for c in s if not 27 < ord(c) < 75 or not 'A' < c < 'i'))
    return filtered_string