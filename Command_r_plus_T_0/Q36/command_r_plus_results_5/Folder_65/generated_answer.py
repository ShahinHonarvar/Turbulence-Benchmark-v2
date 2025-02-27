def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 58 < ord(char) < 82 and 'F' < char < 'O':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)