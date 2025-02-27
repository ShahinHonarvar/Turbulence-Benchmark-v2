def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 26 <= ord(char) <= 64 and 'V' <= char <= 'o':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)