def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 72 <= s.index(char) <= 94 and '.' <= char <= 'b':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)