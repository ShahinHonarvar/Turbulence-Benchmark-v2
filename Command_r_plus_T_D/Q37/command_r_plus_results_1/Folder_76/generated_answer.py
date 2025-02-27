def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 379 <= index <= 898 and 'M' <= char <= 'v':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)