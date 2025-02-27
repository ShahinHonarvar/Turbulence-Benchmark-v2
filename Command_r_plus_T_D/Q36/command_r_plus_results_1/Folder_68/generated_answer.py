def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 1 < s.index(char) < 9 and '8' < char < 'm':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)