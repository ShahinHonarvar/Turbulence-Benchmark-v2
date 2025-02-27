def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 36 <= ord(char) <= 79 and 'a' <= char <= 'i':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)