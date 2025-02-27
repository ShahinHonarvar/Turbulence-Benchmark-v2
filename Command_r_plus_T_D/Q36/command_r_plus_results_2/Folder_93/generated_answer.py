def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 52 < s.index(char) < 88 and ord(char) > ord('&') and (ord(char) < ord('c')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)