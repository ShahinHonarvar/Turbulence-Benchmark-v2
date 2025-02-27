def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if i < 124 or i > 854 or (char < '9' or char > 's'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)