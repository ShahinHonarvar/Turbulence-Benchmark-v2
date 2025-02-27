def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if i < 24 or i > 79 or (char < 'a' or char > 'f'):
            filtered_string.append(char)
    return ''.join(filtered_string)