def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 17 <= index <= 63 and 'O' <= char <= '^':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)