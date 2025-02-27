def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 34 <= i <= 67 and 'W' <= char <= 'x':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)