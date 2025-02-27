def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 11 <= index <= 72 and 'i' <= char <= 'v':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)