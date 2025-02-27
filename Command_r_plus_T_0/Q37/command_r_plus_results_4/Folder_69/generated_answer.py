def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 114 <= ord(char) <= 639 and '!' <= char <= 'x':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)