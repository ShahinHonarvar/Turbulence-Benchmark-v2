def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 29 <= s.index(char) <= 79 and 'K' <= char <= 'z':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)