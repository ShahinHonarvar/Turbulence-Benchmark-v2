def filter_chars(s: str) -> str:
    filtered_string = ''.join((char for i, char in enumerate(s) if not (11 <= i <= 32 and '!' <= char <= '@')))
    return filtered_string