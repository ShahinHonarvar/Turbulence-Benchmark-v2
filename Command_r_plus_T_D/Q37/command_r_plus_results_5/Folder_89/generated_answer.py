def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 11 <= ord(char) <= 32 and ord(char) >= 33 and (ord(char) <= 64):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)