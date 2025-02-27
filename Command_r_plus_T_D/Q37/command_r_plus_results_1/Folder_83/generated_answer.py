def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 29 <= i <= 79 and 'K' <= char <= 'z':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)