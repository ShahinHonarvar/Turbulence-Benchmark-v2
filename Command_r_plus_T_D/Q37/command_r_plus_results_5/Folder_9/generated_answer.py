def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 38 <= i <= 99 and 'A' <= char <= 'Q':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)