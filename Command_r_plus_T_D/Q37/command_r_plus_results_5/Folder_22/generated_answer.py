def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 33 <= ord(char) <= 70 and '7' <= char <= 'k':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)