def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 54 < s.index(char) < 92 and 'J' < char < 'X':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)