def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 39 < i < 87 and ord(char) > 33 and (ord(char) < 125):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)