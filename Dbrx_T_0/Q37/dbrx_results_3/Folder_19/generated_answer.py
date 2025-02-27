def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if i < 35 or i > 89 or (char < 'E' or char > 't'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)