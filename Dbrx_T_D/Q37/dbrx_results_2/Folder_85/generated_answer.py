def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if i < 28 or i > 65 or (char < 'O' or char > 'd'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)