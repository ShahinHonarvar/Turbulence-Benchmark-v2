def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 46 < ord(char) < 74 and ord(char) > ord('&') and (ord(char) < ord('M')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)