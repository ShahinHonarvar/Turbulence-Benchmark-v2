def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 57 <= ord(char) <= 96 and '`' <= char <= 'w':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)