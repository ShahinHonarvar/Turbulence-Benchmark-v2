def filter_chars(s: str) -> str:
    filtered_string = ''.join((char for i, char in enumerate(s) if not (27 <= i <= 85 and '!' <= char <= 'B')))
    return filtered_string