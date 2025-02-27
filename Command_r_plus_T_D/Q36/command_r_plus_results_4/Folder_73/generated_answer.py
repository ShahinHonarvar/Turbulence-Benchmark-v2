def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 66 < ord(char) < 90 and '#' < char < 'T':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)