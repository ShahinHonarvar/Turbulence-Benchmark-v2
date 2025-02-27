def filter_chars(s: str) -> str:
    filtered_string = ''.join((c for i, c in enumerate(s) if not (11 <= i <= 32 and 33 <= ord(c) <= 64)))
    return filtered_string