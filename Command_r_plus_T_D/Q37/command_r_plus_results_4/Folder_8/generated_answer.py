def filter_chars(s: str) -> str:
    filtered_string = ''.join((char for i, char in enumerate(s) if not (41 <= i <= 86 and 'S' <= char <= 's')))
    return filtered_string