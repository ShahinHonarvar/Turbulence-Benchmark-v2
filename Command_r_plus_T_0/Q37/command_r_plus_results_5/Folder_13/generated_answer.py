def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 124 <= index <= 854 and '9' <= char <= 's':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)