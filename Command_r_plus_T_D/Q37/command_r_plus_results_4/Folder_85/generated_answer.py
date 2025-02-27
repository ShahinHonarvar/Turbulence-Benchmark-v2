def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 28 <= ord(char) <= 65 and 'O' <= char <= 'd':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)