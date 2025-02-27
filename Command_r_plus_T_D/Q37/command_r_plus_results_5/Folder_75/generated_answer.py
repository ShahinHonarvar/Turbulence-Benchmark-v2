def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 34 <= index <= 67 and 'W' <= char <= 'x':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)