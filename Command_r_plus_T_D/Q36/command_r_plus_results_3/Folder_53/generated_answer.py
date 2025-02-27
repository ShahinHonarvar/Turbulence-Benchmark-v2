def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 90 < ord(char) < 97 and 'j' < char < 'w':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)