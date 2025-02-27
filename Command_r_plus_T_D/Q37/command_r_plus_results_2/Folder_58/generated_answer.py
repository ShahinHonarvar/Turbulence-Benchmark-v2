def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 503 <= i <= 753 and '9' <= char <= 'w':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)