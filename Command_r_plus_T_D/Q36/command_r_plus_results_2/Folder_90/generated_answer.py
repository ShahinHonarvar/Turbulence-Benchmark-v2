def filter_chars(s: str) -> str:
    filtered_chars = []
    for char in s:
        if 344 < s.index(char) < 874 and 'f' < char < '~':
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)