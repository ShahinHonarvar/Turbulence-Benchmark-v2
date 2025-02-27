def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 23 <= i <= 89 and 'w' <= char <= '{':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)