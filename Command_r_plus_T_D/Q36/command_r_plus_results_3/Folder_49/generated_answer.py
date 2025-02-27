def filter_chars(s: str) -> str:
    filtered_string = ''
    for char in s:
        if 46 < ord(char) < 91 and 'D' < char < 'H':
            continue
        filtered_string += char
    return filtered_string