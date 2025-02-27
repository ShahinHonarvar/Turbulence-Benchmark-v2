def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if i < 379 or i > 898 or (char < 'M' or char > 'v'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)