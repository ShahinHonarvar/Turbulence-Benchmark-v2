def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 19 <= index <= 92 and '8' <= char <= 'm':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)