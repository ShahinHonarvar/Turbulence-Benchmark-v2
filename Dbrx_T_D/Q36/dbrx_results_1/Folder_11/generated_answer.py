def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if 86 < i < 93:
            if not 'E' < char < '~':
                filtered_chars.append(char)
        else:
            filtered_chars.append(char)
    return ''.join(filtered_chars)