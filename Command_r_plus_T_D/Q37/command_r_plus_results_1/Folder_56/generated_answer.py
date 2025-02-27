def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 71 <= ord(char) <= 94 and 'K' <= char <= 'a':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)