def filter_chars(s: str) -> str:
    filtered_string = ''
    for char in s:
        if 31 < ord(char) < 70 and ord(char) > ord('B') and (ord(char) < ord('v')):
            continue
        filtered_string += char
    return filtered_string