def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 35 <= index <= 98 and 'A' <= char <= 'b':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)