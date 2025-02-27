def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 35 <= s.index(char) <= 98 and 'A' <= char <= 'b':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)