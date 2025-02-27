def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 225 <= ord(char) <= 381 and 'D' <= char <= 'Y':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)