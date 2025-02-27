def filter_chars(s: str) -> str:
    filtered_string = ''.join((char for i, char in enumerate(s) if i < 12 or i > 88 or (char < '&' or char > 'v')))
    return filtered_string