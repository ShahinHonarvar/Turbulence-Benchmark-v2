def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 138 <= i <= 920 and '6' <= char <= 'A':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)