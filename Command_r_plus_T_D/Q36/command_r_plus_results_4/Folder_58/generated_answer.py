def filter_chars(s: str) -> str:
    filtered_chars = []
    for char in s:
        if 318 < s.index(char) < 337 and 'B' < char < 'z':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)