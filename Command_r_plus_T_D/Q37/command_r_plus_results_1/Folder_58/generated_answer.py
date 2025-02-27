def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 503 <= s.index(char) <= 753 and '9' <= char <= 'w':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)