def filter_chars(s: str) -> str:
    filtered_string = ''.join((char for i, char in enumerate(s) if not (25 <= i <= 97 and 'm' <= char <= 'w')))
    return filtered_string