def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 41 <= s.index(char) <= 86 and 'S' <= char <= 's':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)