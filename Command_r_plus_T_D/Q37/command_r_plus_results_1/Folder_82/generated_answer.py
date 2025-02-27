def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 12 <= s.index(char) <= 25 and 'P' <= char <= 'x':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)