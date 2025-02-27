def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 17 <= i <= 63 and 'O' <= char <= '^':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)