def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 20 <= index <= 79 and '!' <= char <= 'T':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)