def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 18 <= s.index(char) <= 81 and 'W' <= char <= '[':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)