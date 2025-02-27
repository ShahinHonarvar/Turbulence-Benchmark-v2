def filter_chars(s: str) -> str:
    filtered_chars = ''
    for i, char in enumerate(s):
        if i < 5 or i > 6 or (char < 'G' or char > 'p'):
            filtered_chars += char
    return filtered_chars