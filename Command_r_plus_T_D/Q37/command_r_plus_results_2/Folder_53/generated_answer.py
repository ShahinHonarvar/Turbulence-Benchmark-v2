def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 83 <= ord(char) <= 99 and '*' <= char <= 'j':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)