def filter_chars(s: str) -> str:
    filtered_chars = []
    for char in s:
        if 476 < s.index(char) < 948 and 'b' < char < 'd':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)