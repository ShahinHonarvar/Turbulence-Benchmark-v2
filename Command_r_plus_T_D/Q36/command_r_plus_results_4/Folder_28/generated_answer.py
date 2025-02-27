def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 31 < ord(char) < 73 and ord(char) > ord('M') and (ord(char) < ord('j')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)