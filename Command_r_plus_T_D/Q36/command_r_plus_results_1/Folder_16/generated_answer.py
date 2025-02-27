def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 331 < s.index(char) < 713 and 'M' < char < '_':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)