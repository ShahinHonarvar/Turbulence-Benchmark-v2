def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 43 <= s.index(char) <= 80 and ord(char) >= ord('=') and (ord(char) <= ord('E')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)