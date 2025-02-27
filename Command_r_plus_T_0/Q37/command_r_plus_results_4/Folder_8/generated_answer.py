def filter_chars(s: str) -> str:
    filtered_string = ''.join((char for i, char in enumerate(s) if i < 41 or i > 86 or char < 'S' or (char > 's')))
    return filtered_string