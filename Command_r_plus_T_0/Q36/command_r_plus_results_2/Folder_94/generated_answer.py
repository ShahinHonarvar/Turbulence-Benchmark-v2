def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 15 < s.index(char) < 85 and 'I' < char < 'M':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)