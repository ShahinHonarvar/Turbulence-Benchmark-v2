def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 52 <= ord(char) <= 81 and 'A' <= char <= 'U':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)