def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 43 <= i <= 80 and '=' <= char <= 'E':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)